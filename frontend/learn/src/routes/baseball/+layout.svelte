<script>
  // This layout wraps all pages under /baseball
</script>

<style>
  nav {
    background: #d43636;
    padding: 1rem;
    border-bottom: 2px solid #5f5fc5dd;
  }
  ul {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
  }
  li {
    margin-right: 1rem;
  }
  a {
    text-decoration: none;
    color: #333;
  }
  a.active {
    font-weight: bold;
  }
</style>

<nav>
  <ul>
    <!-- Links relative to the /baseball root -->
    <li><a href="/baseball">Home</a></li>
    <li><a href="/baseball/teams">Teams</a></li>
    <li><a href="/baseball/games">Games</a></li>
  </ul>
</nav>

<!-- This slot will render the content of nested pages -->
<slot />
