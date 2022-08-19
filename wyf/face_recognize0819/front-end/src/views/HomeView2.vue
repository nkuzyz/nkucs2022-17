<template>
  <div>
    <!-- 顶部通栏 -->
    <AppTopNav/>
    <!--    main-->
    <div>
      在这里塞东西
    </div>
    <!-- bottom -->
    <my-footer>fixed</my-footer>
  </div>
</template>

<script>
import MyFooter from "@/components/MyFooter";
import AppTopNav from '@/components/AppTopNav.vue';
import Button from "@/components/Button";
export default {
  name: "HomeView2",
  components: {
    MyFooter,
    AppTopNav
  }
}
</script>

<style scoped>

</style>