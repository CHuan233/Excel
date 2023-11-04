<template>
  <NConfigProvider
    :theme="darkTheme"
    :theme-overrides="themeOverrides"
    class="overflow-y-auto font-mono"
  >
    <div class="h-screen font-major bg-bottom flex text-white text-base">
      <nav
        class="flex-none flex-col flex items-center py-8 gap-4 relative transition-all"
        :class="closed ? 'w-[60px] px-1' : 'w-[200px] px-2'"
      >
        <div v-for="nav in navs" class="w-full flex overflow-hidden">
          <RouterLink
            :to="nav.path"
            v-if="!nav.children"
            class="p-2 px-4 border border-transparent hover:border-white w-full transition-all"
          >
            <div class="flex gap-2 items-center h-8 relative">
              <span
                v-html="nav.icon"
                class="transition-all"
                :class="closed ? 'absolute left-1/2 -translate-x-1/2' : ''"
              ></span>
              <span
                :class="closed ? 'scale-0' : 'scale-100'"
                class="origin-left transition-all"
              >
                {{ nav.label }}
              </span>
            </div>
          </RouterLink>
        </div>
        <button
          class="top-1/2 -translate-y-1/2 -right-2 absolute"
          @click="closed = !closed"
        >
          <i
            v-if="!closed"
            class="ri-arrow-left-s-line hover:text-4xl text-lg transition-all rounded-full border border-white"
          ></i>
          <i
            v-else
            class="ri-arrow-right-s-line hover:text-4xl text-lg transition-all rounded-full border border-white"
          ></i>
        </button>
      </nav>
      <RouterView class="flex-1 h-full overflow-hidden" />
    </div>
  </NConfigProvider>
</template>

<script setup>
import { ref } from "vue";
import { NConfigProvider, darkTheme } from "naive-ui";
import { primaryColor, secondaryColor } from "./color";
/**
 * @type import('naive-ui').GlobalThemeOverrides
 */
const themeOverrides = {
  common: {
    primaryColor,
    primaryColorHover: "#BFE8FFFF",
    primaryColorPressed: "#4190BCFF",
    primaryColorSuppl: "#296E95FF",
  },
  Table: {
    tdColor: "rgba(0,0,0,0)",
    thColor: secondaryColor,
  },
  DataTable: {
    tdColor: "rgba(0,0,0,0)",
    thColor: secondaryColor,
    tdColorHover: "rgb(133,199,236,0.3)",
  },
};

const navs = ref([
  {
    path: "/",
    label: "成绩发送",
    icon: '<i class="ri-home-line text-3xl"></i>',
  },
]);

const closed = ref(true);
</script>

<style>
a.router-link-exact-active {
  @apply bg-gradient-to-br from-primary to-secondary font-bold text-active;
}

.ab-center {
  @apply absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2;
}
</style>
