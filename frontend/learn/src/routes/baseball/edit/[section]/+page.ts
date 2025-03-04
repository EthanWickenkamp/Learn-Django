import type { PageLoad } from './$types.js';

export const load: PageLoad = async ({ fetch, params }) => {
    const { section } = params;
    
    if (!section) { //check if section is empty or undefined
        console.error("Error: Section is undefined in +page.ts!");
        return { section: null, data: [] };
    }

    const res = await fetch(`/api/${section}/`);
    const data = await res.json();

    return { section, data };
};
