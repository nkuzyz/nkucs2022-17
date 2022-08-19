<template>
    <div class="app-top-nav">
        <div class="w">
            <ul>
                <template v-if="userinfo.token">
                    <li><a href="http://localhost:8080/#/user">
                        <i class="iconfont icon-xinrenzhinan"></i>
                        用户
                        </a>
                    </li>
                    <li><a href="http://localhost:8080/#/bye">
                        <i class="iconfont icon-tuichu"></i>
                        退出登录
                        </a>
                    </li>
                </template>
                <li v-else><a href="http://localhost:8080/#/login">
                <i class="iconfont icon-denglu"></i>
                登录
                </a>
                </li>
                <li><a href="http://localhost:8080/#/">
                    <i class="iconfont icon-shouyefill"></i>
                    首页
                    </a>
                </li>
                <li><a href="http://localhost:8080/#/twomethods">
                    <i class="iconfont icon-kaishi"></i>
                    开始体验
                    </a>
                </li>

                <li>
                    <a href="http://localhost:8080/#/about">
                    <i class="iconfont icon-guanyu"></i>
                    关于
                    </a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import {useStore} from 'vuex'
import {computed} from "vue";
export default{
    setup(props) {
        const store = useStore();
        let userinfo = computed(() => {
            return store.state.user.userinfo;
        });
        return {userinfo};
    }
}
</script>

<style lang="less" scoped>
@import url('../assets/styles/variable.less');

.app-top-nav{
    background-color:@xTxColor;
    ul{
        height: 38px;
        line-height: 38px;
        display: flex;
        justify-content: flex-end;
        li{
            a{
                padding: 0 10px;
                color:#fff;
                border-left: 1px solid #fff;
                &:hover{
                    color: @helpColor;
                }
            }
        }
    }
}

</style>