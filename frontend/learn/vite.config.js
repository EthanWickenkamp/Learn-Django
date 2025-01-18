import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	port: 5173,
    host: '0.0.0.0', // Allows access from Docker and localhost
});
