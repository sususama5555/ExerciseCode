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

function testAwait (x) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x);
    }, 2000);
  });
}

async function helloAsync() {
  var x = await testAwait ("hello world");
  console.log(x);
}
helloAsync ();
// hello world