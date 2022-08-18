<template>
    <div>
        <!-- 顶部通栏 -->
        <AppTopNav/>
        <!-- top -->
        <div></div>
        <!-- main -->
        <div class="main">
            <!-- 二级路由 -->
            <router-view/>
          <span class="sent">动态场景下口罩佩戴监测播报与特效提醒系统:)</span>
          <Button type="plain">按钮</Button>
<!--          <img src="../assets/images/bg-img2.png" alt="">-->
        </div>
        <!-- bottom -->
      <my-footer>fixed</my-footer>
    </div>
</template>

<script>
import AppTopNav from '@/components/AppTopNav.vue';
import Button from '@/components/Button.vue';
import MyFooter from "@/components/MyFooter";

export default{
    components:{
      MyFooter,
    AppTopNav,
    Button
}
}
</script>

<style lang="less" scoped>
.main {
  box-sizing: border-box;
  width:100%;
  height:680px;
  background: no-repeat url("../assets/images/bg-img2.png");
  display: flex;
  align-items: center;
}
.main button {
  width:98px;
  height:40px;
}
.sent{
  margin-left:20%;
}


</style>