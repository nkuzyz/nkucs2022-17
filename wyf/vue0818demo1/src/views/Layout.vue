<template>
    <div>
        <!-- 顶部通栏 -->
        <AppTopNav/>
        <!-- top -->
        <div>头部区域</div>
        <!-- main -->
        <div class="main">
            <!-- 二级路由 -->
            <router-view/>
        </div>
        <!-- bottom -->
    </div>
</template>

<script>
import AppTopNav from '@/components/AppTopNav.vue';
import Button from '@/components/Button.vue';

export default{
    components:{
    AppTopNav,
    Button
}
}
</script>

<style lang="less" scoped>

</style>