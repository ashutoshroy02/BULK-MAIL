import streamlit as st
# CSS styles
css = """
<style>
*
{
    margin: 0;
    padding:0;
    box-sizing: border-box;
}
body{
    overflow: hidden;
}
section{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    /* https://lh3.googleusercontent.com/ka_5IYJDRkXZnbptxq64LPuggGL5FM8gnpJlsuSiOQh4b39kMkiRbVfX8iK8bjMg5SLkdfoix09P60wyFjN2=w681-h614 */
    background: url("https://i.postimg.cc/c1Q3njM0/bg2.jpg");
/*   background-color:black; */
    background-size: cover;
}

@keyframes animateBg{
    0%,100%{
        transform: scale(1);
    }
    50%{
        transform: scale(1.2);
    }
}

span{
    position: absolute;
    top:50%;
    left:50%;
    width: 4px;
    height: 4px;
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 0 0 4px rgba(255,255,255,0.1),0 0 0 8px rgba(255,255,255,0.1),0 0 20px rgba(255,255,255,0.1);
    animation: animate 3s linear infinite;
}
span::before{
    content:'';
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 300px;
    height: 1px;
    background: linear-gradient(90deg,#fff,transparent);
}
@keyframes animate
{
    0%
    {
        transform: rotate(315deg) translateX(0);
        opacity: 1;
    }
    70%
    {
        opacity: 1;
    }
    100%
    {
        transform: rotate(315deg) translateX(-1000px);
        opacity: 0;
    }
}
span:nth-child(1){
    top: 0;
    right: 0;
    left: initial;
    animation-delay: 0s;
    animation-duration: 1s;
}
span:nth-child(2){
    top: 0;
    right: 80px;
    left: initial;
    animation-delay: 0.2s;
    animation-duration: 3s;
}
span:nth-child(3){
    top: 80;
    right: 0px;
    left: initial;
    animation-delay: 0.4s;
    animation-duration: 2s;
}
span:nth-child(4){
    top: 0;
    right: 180px;
    left: initial;
    animation-delay: 0.6s;
    animation-duration: 1.5s;
}
span:nth-child(5){
    top: 0;
    right: 400px;
    left: initial;
    animation-delay: 0.8s;
    animation-duration: 2.5s;
}
span:nth-child(6){
    top: 0;
    right: 600px;
    left: initial;
    animation-delay: 1s;
    animation-duration: 3s;
}
span:nth-child(7){
    top: 300px;
    right: 0px;
    left: initial;
    animation-delay: 1.2s;
    animation-duration: 1.75s;
}
span:nth-child(8){
    top: 0px;
    right: 700px;
    left: initial;
    animation-delay: 1.4s;
    animation-duration: 1.25s;
}
span:nth-child(9){
    top: 0px;
    right: 1000px;
    left: initial;
    animation-delay: 0.75s;
    animation-duration: 2.25s;
}
span:nth-child(9){
    top: 0px;
    right: 450px;
    left: initial;
    animation-delay: 2.75s;
    animation-duration: 2.75s;
}
</style>
"""

# HTML content
html = """
<head>
    <meta name="google-adsense-account" content="ca-pub-7603754372960896">
</head>
<body>
        <section>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </section>
</body>
"""


def render_frontend():
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html, unsafe_allow_html=True)
render_frontend()
