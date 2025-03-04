import type { PageLoad } from './$types.js';

export const load: PageLoad = async ({ fetch, params }) => {
  // Extract the section from the URL (e.g., 'items', 'teams', etc.)
  const { section } = params as { section: string };

  if (!section) {
    console.error("No section provided.");
    return { error: "No section provided." };
  }

  try {
    // Fetch the data from your API endpoint
    const response = await fetch(`/api/${section}/`);
    if (!response.ok) {
      const errorMsg = `Error fetching data: ${response.status} ${response.statusText}`;
      console.error(errorMsg);
      return { error: errorMsg };
    }

    // Assume the API returns an array of objects
    const data = await response.json();

    // Dynamically determine the fields to edit
    let fields: string[] = [];
    if (Array.isArray(data) && data.length > 0) {
      fields = Object.keys(data[0]);
    } else if (typeof data === 'object' && data !== null) {
      fields = Object.keys(data);
    }

    return { section, items: data, fields };
  } catch (err) {
    console.error("Unexpected error:", err);
    return { error: "Unexpected error occurred while fetching data." };
  }
};

