new Vue({
    el: "#app",
    template: window.template,
    data: {
        title: "FlaskMVC!",
        formData: {
            account: "admin",
            password: "admin"
        },
        isLogin: false,
    },
    created() {
        // 检查状态
        axios({
            url: "/user/personal",
            method: "get"
        }).then(response => {
            this.isLogin = response.data['ok'];
        });
    },
    methods: {
        onSubmit() {
            // 登录
            axios({
                url: "/user/personal",
                method: "post",
                data: this.formData
            }).then(response => {
                this.isLogin = response.data['ok'];
            });
        }
    },
    computed: {
        loginStateText() {
            return this.isLogin ? "已经登录" : "还未登录";
        },
        loginStateStyle() {
            return this.isLogin ? {
                color: "white",
                backgroundColor: "green"
            } : {
                color: "white",
                backgroundColor: "darkred"
            };
        }
    }
});