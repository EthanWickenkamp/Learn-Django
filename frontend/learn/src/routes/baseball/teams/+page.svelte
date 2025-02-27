<script lang="ts">
    export let data;
  </script>
  
  <h1>Teams</h1>
  <ul>
    {#each data.teams as team}
      <li>
        <!-- Link uses team.slug -->
        <a href={`/baseball/teams/${encodeURIComponent(team.slug)}`}>
          {team.name}
        </a>
      </li>
    {/each}
  </ul>
  