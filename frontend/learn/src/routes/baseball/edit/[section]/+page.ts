import type { PageLoad } from './$types.js';

export const load: PageLoad = async ({ fetch, params }) => {
    console.log("Params received in +page.ts:", params); // Debugging

    const { section } = params;
    if (!section) {
        console.error("Error: Section is undefined in +page.ts!");
        return { section: null, data: [] };
    }

    const res = await fetch(`/api/${section}`);
    const data = await res.json();

    console.log(`Fetched data for section "${section}":`, data);

    return { section, data };
};
