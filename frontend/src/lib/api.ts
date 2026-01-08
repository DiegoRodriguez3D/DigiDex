// API client for backend communication

import type { DigimonListResponse, DigimonDetail, SearchResult } from './types';

const API_BASE = 'http://localhost:8000/api/v1';

async function fetchAPI<T>(endpoint: string): Promise<T> {
    const response = await fetch(`${API_BASE}${endpoint}`);

    if (!response.ok) {
        throw new Error(`API Error: ${response.status} ${response.statusText}`);
    }

    return response.json();
}

export async function getDigimonList(page: number = 0, pageSize: number = 20): Promise<DigimonListResponse> {
    return fetchAPI<DigimonListResponse>(`/digimon?page=${page}&pageSize=${pageSize}`);
}

export async function getDigimonDetail(idOrName: string | number): Promise<DigimonDetail> {
    return fetchAPI<DigimonDetail>(`/digimon/${encodeURIComponent(idOrName)}`);
}

export async function searchDigimon(name: string): Promise<SearchResult> {
    return fetchAPI<SearchResult>(`/digimon/search?name=${encodeURIComponent(name)}`);
}
