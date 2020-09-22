// @File  :debounce.py
// @Author:Sapphire
// @Date  :2020/9/22 10:07
// @Desc  :前端防抖，在一定时间间隔内函数被触发多次，但只执行最后一次。
function debounce(fn, delay) {
    let timer = null;

    return function() {
        const context = this;
        const args = arguments;

        if (timer) {
            clearTimeout(timer);
            timer = null;
        }

        timer = setTimeout(() => {
            fn.apply(context, args);
        }, delay);
    };
}

const task = () => {console.log("run task")}
const debounceTask  = debounce(task, 1000)
window.addEventListener('scroll', debounceTask)
