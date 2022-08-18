<template>
    <div>
        <!-- 顶部通栏 -->
        <AppTopNav/>
        <!-- 背景图 -->
        <Bg1></Bg1>
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

</style>