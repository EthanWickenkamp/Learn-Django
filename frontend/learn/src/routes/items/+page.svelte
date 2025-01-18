<script>
    import { onMount } from 'svelte';

    let items = []; // Store items fetched from the API

    // Fetch items from Django API
    onMount(async () => {
        try {
            const response = await fetch('api/items/');
            if (response.ok) {
                items = await response.json();
            } else {
                console.error('Failed to fetch items:', response.status);
            }
        } catch (error) {
            console.error('Error fetching items:', error);
        }
    });
</script>

<h1>Item List</h1>

{#if items.length > 0}
    <ul>
        {#each items as item}
            <li>
                <strong>{item.name}</strong>: {item.description}
            </li>
        {/each}
    </ul>
{:else}
    <p>No items available</p>
{/if}
