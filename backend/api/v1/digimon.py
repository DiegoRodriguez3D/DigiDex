"""Digimon API endpoints."""

from fastapi import APIRouter, HTTPException, Query
import httpx

from schemas.digimon import (
    DigimonListItem,
    DigimonListResponse,
    DigimonDetail,
    SkillSchema,
    FieldSchema,
    EvolutionSchema,
    PaginationInfo,
)
from services.digi_api import digi_api_client

router = APIRouter(prefix="/digimon", tags=["digimon"])


def extract_list_item(raw: dict, detail: dict | None = None) -> DigimonListItem:
    """Transform raw API response to clean list item."""
    level = None
    attribute = None

    if detail:
        # Extract from detail response
        if detail.get("levels"):
            level = detail["levels"][0].get("level")
        if detail.get("attributes"):
            attribute = detail["attributes"][0].get("attribute")
    
    return DigimonListItem(
        id=raw["id"],
        name=raw["name"],
        image=raw.get("image", ""),
        level=level,
        attribute=attribute,
    )


def extract_detail(raw: dict) -> DigimonDetail:
    """Transform raw API response to clean detail schema."""
    # Extract first level and attribute
    level = None
    attribute = None
    
    if raw.get("levels"):
        level = raw["levels"][0].get("level")
    if raw.get("attributes"):
        attribute = raw["attributes"][0].get("attribute")
    
    # Extract types
    types = [t["type"] for t in raw.get("types", []) if t.get("type")]
    
    # Extract English description
    description = None
    for desc in raw.get("descriptions", []):
        if desc.get("language") == "en_us":
            description = desc.get("description")
            break
    
    # Extract skills
    skills = [
        SkillSchema(
            id=s["id"],
            name=s["skill"],
            description=s.get("description"),
        )
        for s in raw.get("skills", [])[:10]  # Limit to 10 skills
    ]
    
    # Extract fields
    fields = [
        FieldSchema(
            id=f["id"],
            name=f["field"],
            image=f.get("image"),
        )
        for f in raw.get("fields", [])
    ]
    
    # Extract evolutions (filter out nulls)
    prior_evolutions = [
        EvolutionSchema(
            id=e["id"],
            name=e["digimon"],
            image=e["image"],
            condition=e.get("condition") or None,
        )
        for e in raw.get("priorEvolutions", [])
        if e.get("id") and e.get("digimon") and e.get("image")
    ][:10]  # Limit to 10
    
    next_evolutions = [
        EvolutionSchema(
            id=e["id"],
            name=e["digimon"],
            image=e["image"],
            condition=e.get("condition") or None,
        )
        for e in raw.get("nextEvolutions", [])
        if e.get("id") and e.get("digimon") and e.get("image")
    ][:10]  # Limit to 10
    
    # Get image
    image = ""
    if raw.get("images"):
        image = raw["images"][0].get("href", "")
    
    return DigimonDetail(
        id=raw["id"],
        name=raw["name"],
        image=image,
        level=level,
        attribute=attribute,
        types=types,
        description=description,
        skills=skills,
        fields=fields,
        prior_evolutions=prior_evolutions,
        next_evolutions=next_evolutions,
    )


@router.get("", response_model=DigimonListResponse)
async def get_digimon_list(
    page: int = Query(default=0, ge=0, description="Page number"),
    page_size: int = Query(default=20, ge=1, le=100, description="Items per page"),
):
    """Get paginated list of Digimon for the grid view."""
    try:
        data = await digi_api_client.get_digimon_list(page=page, page_size=page_size)
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Failed to fetch Digimon list")
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Digi-API unavailable")
    
    raw_content = data.get("content", [])
    pageable = data.get("pageable", {})
    
    # For the list view, we just return basic info
    # Attribute/level require individual fetches, so we skip them for performance
    content = [
        DigimonListItem(
            id=item["id"],
            name=item["name"],
            image=item.get("image", ""),
            level=None,
            attribute=None,
        )
        for item in raw_content
    ]
    
    pagination = PaginationInfo(
        current_page=pageable.get("currentPage", page),
        total_pages=pageable.get("totalPages", 0),
        total_elements=pageable.get("totalElements", 0),
        has_next=bool(pageable.get("nextPage")),
        has_previous=bool(pageable.get("previousPage")),
    )
    
    return DigimonListResponse(content=content, pagination=pagination)


@router.get("/search")
async def search_digimon(
    name: str = Query(..., min_length=1, description="Digimon name to search"),
):
    """Search Digimon by name."""
    try:
        data = await digi_api_client.search_digimon(name=name)
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Search failed")
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Digi-API unavailable")
    
    raw_content = data.get("content", [])
    
    content = [
        DigimonListItem(
            id=item["id"],
            name=item["name"],
            image=item.get("image", ""),
            level=None,
            attribute=None,
        )
        for item in raw_content
    ]
    
    return {"results": content}


@router.get("/{id_or_name}", response_model=DigimonDetail)
async def get_digimon_detail(id_or_name: str):
    """Get detailed info for a single Digimon."""
    try:
        data = await digi_api_client.get_digimon_detail(id_or_name)
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"Digimon '{id_or_name}' not found")
        raise HTTPException(status_code=e.response.status_code, detail="Failed to fetch Digimon")
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Digi-API unavailable")
    
    return extract_detail(data)
