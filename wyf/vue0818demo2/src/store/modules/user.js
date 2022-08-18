export default{
    namespaced: true,
    state:()=>{
        return{
            userinfo: {
                token:'123',
                username:'龙老师'
            }
        }
    },
    mutations:{
        updateName(state,username){
            state.userinfo.username = username;
        }
    },
    actions:{
        updateNameAsync({commit}){
            setTimeout(()=>{
                commit('updateName','张三');
            },1000)
        }

    }
}