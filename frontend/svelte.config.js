import { vitePreprocess } from '@sveltejs/vite-plugin-svelte'
import adapter from '@sveltejs/adapter-node'

export default {
  // Consult https://svelte.dev/docs#compile-time-svelte-preprocess
  // for more information about preprocessors
  preprocess: vitePreprocess(),
}
