<template>
    <div>
        <!-- 顶部通栏 -->
        <AppTopNav fixed/>
        <!-- 背景图 -->
        <div class="aboutbg">
            <div class="aboutword1">
                Hello
            </div>
            <div class="aboutword2">
                你好:)
            </div>
        </div>
        <!-- <Bg1></Bg1> -->
        <!-- footer -->
        <MyFooter>fixed</MyFooter>
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
    //background: url(../assets/images/bg-img3.png) no-repeat center;
    //background-size: cover;
    //height: 100%;
    //width: 100%;
    //position: fixed;
    //background-size: 100% 100%;
    box-sizing: border-box;
    width:100%;
    height:680px;
    background: no-repeat url("../assets/images/bg-img3.jpg");
    display: flex;
    align-items: center;
}

.aboutword1{
    position: absolute;
    top: 30%;
    left: 47%;
    transform: translate(-30%,-30%);
    font-size: 60px;
    color: #fff;
    font-weight: bold;
}

.aboutword2{
    position: absolute;
    top: 50%;
    left: 47%;
    transform: translate(-30%,-30%);
    font-size: 40px;
    color: #fff;
    font-weight: bold;
}

</style>