<script lang="ts">
    export let section;
    export let data;
  
    console.log("Section in Svelte:", section);
    console.log("Data in Svelte:", data);
  </script>
  
  <h1>Edit {section}</h1>
  
  <!-- Debugging output -->
  <pre>{JSON.stringify(data, null, 2)}</pre>
  
  {#if data && Array.isArray(data) && data.length > 0}
    <ul>
      {#each data as item}
        <li>
          <input type="text" bind:value={item.name} />
          <input type="text" bind:value={item.description} />
          <button on:click={() => saveItem(item.id, { name: item.name, description: item.description })}>Save</button>
        </li>
      {/each}
    </ul>
  {:else}
    <p>No {section} available.</p>
  {/if}
  