<template>
    <div>
        <!-- 顶部通栏 -->
        <AppTopNav fixed/>
        <!-- 背景图 -->
        <div class="aboutbg">
            <div class="aboutword">
                关于
            </div>
        </div>
        <!-- <Bg1></Bg1> -->
        <!-- footer -->
        <MyFooter fixed></MyFooter>
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

.aboutbg{
    background: url(../assets/images/bg-img3.png) no-repeat center;
    background-size: cover;
    height: 100%;
    width: 100%;
    position: fixed;
    background-size: 100% 100%;
}

.aboutword{
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translate(-30%,-30%);
    font-size: 50px;
    color: #fff;
    font-weight: bold;
}

</style>