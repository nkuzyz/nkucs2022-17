<template>
    <div>
        <h2>布局</h2>
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
        <div>底部区域</div>
    </div>
</template>

<script>
import AppTopNavVue from '@/components/AppTopNav.vue';
import AppTopNav from '@/components/AppTopNav.vue';
export default{
    components:{
    AppTopNav
}
}
</script>

<style lang="less" scoped>

</style>