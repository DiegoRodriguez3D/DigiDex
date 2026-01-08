import type { PageServerLoad } from './$types';
import type { DigimonDetail } from '$lib/types';
import { env } from '$env/dynamic/private';

const API_BASE = env.API_URL || 'http://localhost:8000/api/v1';

export const load: PageServerLoad = async ({ params, fetch }) => {
    const { id } = params;

    try {
        const response = await fetch(`${API_BASE}/digimon/${encodeURIComponent(id)}`);

        if (!response.ok) {
            if (response.status === 404) {
                return {
                    digimon: null,
                    error: `Digimon "${id}" not found in the database.`
                };
            }
            throw new Error(`API Error: ${response.status}`);
        }

        const digimon: DigimonDetail = await response.json();

        return {
            digimon,
            error: null
        };
    } catch (error) {
        console.error('Failed to load Digimon detail:', error);
        return {
            digimon: null,
            error: 'Failed to connect to DigiDex API. Please ensure the backend is running.'
        };
    }
};
