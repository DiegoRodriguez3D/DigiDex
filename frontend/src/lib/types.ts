// Type definitions for DigiDex frontend

export interface DigimonListItem {
    id: number;
    name: string;
    image: string;
    level: string | null;
    attribute: string | null;
}

export interface Skill {
    id: number;
    name: string;
    description: string | null;
}

export interface Field {
    id: number;
    name: string;
    image: string | null;
}

export interface Evolution {
    id: number;
    name: string;
    image: string;
    condition: string | null;
}

export interface DigimonDetail {
    id: number;
    name: string;
    image: string;
    level: string | null;
    attribute: string | null;
    types: string[];
    description: string | null;
    skills: Skill[];
    fields: Field[];
    prior_evolutions: Evolution[];
    next_evolutions: Evolution[];
}

export interface Pagination {
    current_page: number;
    total_pages: number;
    total_elements: number;
    has_next: boolean;
    has_previous: boolean;
}

export interface DigimonListResponse {
    content: DigimonListItem[];
    pagination: Pagination;
}

export interface SearchResult {
    results: DigimonListItem[];
}
