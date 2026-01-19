import type { LayoutServerLoad } from './$types';
import { env } from '$env/dynamic/private';

export const load: LayoutServerLoad = async () => {
    return {
        portfolioUrl: env.PORTFOLIO_URL || 'https://diego-rodriguez.es'
    };
};
