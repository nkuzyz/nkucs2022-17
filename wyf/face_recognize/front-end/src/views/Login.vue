<template>
    <div>
        <!-- 顶部通栏 -->
        <AppTopNav/>
        <!-- 背景图 -->
        <!-- <Bg1></Bg1> -->
        <span>nihao</span>
        <div class="loginbg">
            
        </div>
        <!-- footer -->
        <MyFooter></MyFooter>
    </div>
</template>

<script>
import AppTopNav from '@/components/AppTopNav.vue';
import MyFooter from '@/components/MyFooter.vue';
import Bg1 from '@/components/bg1.vue';
export default{
    components:{
    AppTopNav,
    MyFooter,
    Bg1
}
}
</script>

<style lang="less" scoped>

.loginbg{
    background: url(../assets/images/bg-img3.png) no-repeat center;
    height: 100%;
    width: 100%;
    //position: fixed;
    background-size: 100% 100% !important;
}

</style>