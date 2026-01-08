// +page.server.ts - Server-side data loading for home page
import type { PageServerLoad } from './$types';
import type { DigimonListResponse, DigimonListItem } from '$lib/types';

const API_BASE = 'http://localhost:8000/api/v1';

export const load: PageServerLoad = async ({ url, fetch }) => {
    const page = parseInt(url.searchParams.get('page') || '0', 10);
    const search = url.searchParams.get('search') || '';
    const pageSize = 32;

    try {
        if (search) {
            // Search mode
            const response = await fetch(`${API_BASE}/digimon/search?name=${encodeURIComponent(search)}`);

            if (!response.ok) {
                throw new Error(`API Error: ${response.status}`);
            }

            const data = await response.json();

            return {
                digimon: data.results as DigimonListItem[],
                pagination: null,
                searchQuery: search,
                error: null
            };
        } else {
            // Paginated list mode
            const response = await fetch(`${API_BASE}/digimon?page=${page}&pageSize=${pageSize}`);

            if (!response.ok) {
                throw new Error(`API Error: ${response.status}`);
            }

            const data: DigimonListResponse = await response.json();

            return {
                digimon: data.content,
                pagination: data.pagination,
                searchQuery: null,
                error: null
            };
        }
    } catch (error) {
        console.error('Failed to load Digimon:', error);
        return {
            digimon: [],
            pagination: null,
            searchQuery: search || null,
            error: 'Failed to connect to DigiDex API. Please ensure the backend is running.'
        };
    }
};
