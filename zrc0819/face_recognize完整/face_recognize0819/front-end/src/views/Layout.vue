<template>
    <div>
        <!-- 顶部通栏 -->
        <AppTopNav/>
        <!-- main -->
        <div class="main">
            <span class="sent">动态场景下口罩佩戴监测播报与特效提醒系统:)</span>
        </div>
        <!-- bottom -->
      <my-footer>fixed</my-footer>
    </div>
</template>

<script>
import AppTopNav from '@/components/AppTopNav.vue';
import MyFooter from "@/components/MyFooter";

export default{
    components:{
      MyFooter,
    AppTopNav
}
}
</script>

<style lang="less" scoped>
.main {
  box-sizing: border-box;
  width:100%;
  height:680px;
  background: no-repeat url("../assets/images/bg-img2.jpg");
  display: flex;
  align-items: center;
}
.main button {
  width:98px;
  height:40px;
}
.sent{
  width:660px;
    position: absolute;
    top: 50%;
    left: 30%;
    transform: translate(-50%,-70%);
    color: #fff;
    font-size: 50px;
    font-weight: bold;
    text-align: center;

}


</style>