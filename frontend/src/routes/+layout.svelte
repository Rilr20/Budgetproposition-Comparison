<script lang="ts">
    import '../app.scss';
    import Footer from '$lib/footer.svelte';
    import Navbar from '$lib/navbar.svelte';
</script>

<Navbar />
<slot></slot>
<Footer />
