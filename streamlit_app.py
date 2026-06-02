import streamlit as st
import math
from sympy import symbols, expand, binomial, latex
from sympy import sympify

st.set_page_config(page_title="이항정리 학습도구", layout="wide")

st.title("� 이항정리 & 파스칼의 삼각형 학습도구")
st.markdown("""
이 교육 도구에서는 **이항정리(Binomial Theorem)**와 **파스칼의 삼각형(Pascal's Triangle)**을 단계별로 학습할 수 있습니다.

**📖 페이지 구성:**
- 🏠 **홈** (현재 페이지): 이항정리 계산 및 연습문제
- 🔺 **파스칼의 삼각형**: 삼각형 생성과 이항정리와의 관계
""")

st.markdown("---")

# 탭 구성
tab1, tab2 = st.tabs(["이항정리 계산", "연습문제"])

with tab1:
    st.markdown("## 이항정리 전개")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        n = st.number_input("지수 n 입력:", min_value=0, max_value=10, value=3, step=1)
    with col2:
        a_var = st.text_input("a의 계수 (기본값: 1):", value="1")
    with col3:
        b_var = st.text_input("b의 계수 (기본값: 1):", value="1")
    
    if st.button("전개하기", key="expand_btn", use_container_width=True):
        try:
            a, b, x, y = symbols('a b x y')
            
            # 이항정리 공식 표시
            st.markdown(f"### (a+b)^{n} 전개")
            
            # 이항정리 수식 표시
            st.latex(f"(a+b)^{n} = \\sum_{{k=0}}^{{{n}}} \\binom{{{n}}}{{k}} a^{{{n}-k}} b^{{k}}")
            
            st.markdown("**전개 과정:**")
            
            # 각 항을 계산하여 표시
            terms = []
            expansion_steps = []
            
            for k in range(n + 1):
                coeff = math.comb(n, k)
                power_a = n - k
                power_b = k
                
                # 단계별 표현
                if power_a == 0:
                    term_str = f"\\binom{{{n}}}{{{k}}} b^{{{power_b}}}"
                    term_display = f"{coeff}b^{power_b}"
                elif power_b == 0:
                    term_str = f"\\binom{{{n}}}{{{k}}} a^{{{power_a}}}"
                    term_display = f"{coeff}a^{power_a}"
                else:
                    term_str = f"\\binom{{{n}}}{{{k}}} a^{{{power_a}}} b^{{{power_b}}}"
                    term_display = f"{coeff}a^{power_a}b^{power_b}"
                
                expansion_steps.append(f"**항 {k+1}:** {coeff}a^{power_a}b^{power_b}" if (power_a > 0 and power_b > 0) else 
                                     f"**항 {k+1}:** {coeff}b^{power_b}" if power_a == 0 else 
                                     f"**항 {k+1}:** {coeff}a^{power_a}")
                terms.append(term_str)
            
            # 전개 과정 표시
            step_text = " + ".join(terms)
            st.latex(step_text)
            
            # 상세 단계
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**각 항의 계수:**")
                for step in expansion_steps:
                    st.markdown(step)
            
            # 최종 답
            st.markdown("**최종 답:**")
            final_answer = " + ".join([f"{math.comb(n, k)}a^{n-k}b^{k}" if (n-k > 0 and k > 0) else 
                                      f"{math.comb(n, k)}b^{k}" if n-k == 0 else 
                                      f"{math.comb(n, k)}a^{n-k}" for k in range(n+1)])
            st.success(f"(a+b)^{n} = {final_answer}")
            
        except Exception as e:
            st.error(f"오류 발생: {str(e)}")

with tab2:
    st.markdown("## 🎯 연습문제")
    st.markdown("다음 문제들을 풀어보세요!")
    
    # 문제 1
    st.markdown("### 문제 1")
    st.markdown("**(x+y)^2** 를 전개하시오.")
    
    with st.expander("정답 확인"):
        st.latex("(x+y)^2 = x^2 + 2xy + y^2")
        st.markdown("""
        **풀이:**
        - 항 1: $\\binom{2}{0}x^2y^0 = 1 \\cdot x^2 = x^2$
        - 항 2: $\\binom{2}{1}x^1y^1 = 2 \\cdot xy = 2xy$
        - 항 3: $\\binom{2}{2}x^0y^2 = 1 \\cdot y^2 = y^2$
        """)
    
    st.markdown("")
    
    # 문제 2
    st.markdown("### 문제 2")
    st.markdown("**(a-b)^3** 를 전개하시오. (힌트: -b로 생각하면 됩니다)")
    
    with st.expander("정답 확인"):
        st.latex("(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3")
        st.markdown("""
        **풀이:**
        (a+(-b))^3 으로 생각하면:
        - 항 1: $\\binom{3}{0}a^3(-b)^0 = a^3$
        - 항 2: $\\binom{3}{1}a^2(-b)^1 = 3 \\cdot a^2 \\cdot (-b) = -3a^2b$
        - 항 3: $\\binom{3}{2}a^1(-b)^2 = 3 \\cdot a \\cdot b^2 = 3ab^2$
        - 항 4: $\\binom{3}{3}a^0(-b)^3 = -b^3$
        """)
    
    st.markdown("")
    
    # 문제 3
    st.markdown("### 문제 3")
    st.markdown("**(2x+1)^4** 를 전개하시오.")
    
    with st.expander("정답 확인"):
        st.latex("(2x+1)^4 = 16x^4 + 32x^3 + 24x^2 + 8x + 1")
        st.markdown("""
        **풀이:**
        - 항 1: $\\binom{4}{0}(2x)^4(1)^0 = 1 \\cdot 16x^4 = 16x^4$
        - 항 2: $\\binom{4}{1}(2x)^3(1)^1 = 4 \\cdot 8x^3 = 32x^3$
        - 항 3: $\\binom{4}{2}(2x)^2(1)^2 = 6 \\cdot 4x^2 = 24x^2$
        - 항 4: $\\binom{4}{3}(2x)^1(1)^3 = 4 \\cdot 2x = 8x$
        - 항 5: $\\binom{4}{4}(2x)^0(1)^4 = 1$
        """)
    
    st.markdown("")
    st.info("💡 위의 '이항정리 계산' 탭에서 직접 계산하여 답을 확인해볼 수 있습니다!")

st.markdown("---")

st.markdown("""
### 📌 다음 단계
좌측 사이드바의 **🔺 파스칼의 삼각형** 페이지에서:
- 파스칼의 삼각형이 만들어지는 과정 확인
- 이항정리와의 관계 이해
- 삼각형의 성질 탐구

를 할 수 있습니다! ✨
""")
