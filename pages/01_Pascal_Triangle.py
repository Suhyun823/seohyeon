import streamlit as st
import math
import numpy as np

st.set_page_config(page_title="파스칼의 삼각형", layout="wide")

st.title("🔺 파스칼의 삼각형 (Pascal's Triangle)")
st.markdown("**이항정리와 파스칼의 삼각형의 관계를 이해해봅시다!**")

st.markdown("---")

# 탭 구성
tab1, tab2 = st.tabs(["삼각형 생성", "이항정리와의 관계"])

with tab1:
    st.subheader("파스칼의 삼각형 생성")
    
    col1, col2 = st.columns(2)
    with col1:
        rows = st.number_input("행의 개수 (n):", min_value=1, max_value=15, value=8, step=1)
    
    st.markdown("#### 생성 규칙")
    st.markdown("""
    1. **첫 번째 행:** 1
    2. **마지막 행:** 모든 끝이 1
    3. **중간 요소:** 위 행의 인접한 두 수의 합
    
    즉, **위치 (n, k)의 값 = 위치 (n-1, k-1) + 위치 (n-1, k)**
    """)
    
    st.latex("P(n, k) = P(n-1, k-1) + P(n-1, k)")
    
    st.markdown("---")
    
    # 파스칼의 삼각형 생성
    def generate_pascal_triangle(n):
        triangle = []
        for i in range(n):
            row = [1]
            if i > 0:
                for j in range(1, i):
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
                row.append(1)
            triangle.append(row)
        return triangle
    
    pascal = generate_pascal_triangle(rows)
    
    # 시각화 방식 선택
    display_type = st.radio("표시 방식:", ["삼각형", "표"], horizontal=True)
    
    if display_type == "삼각형":
        st.markdown("#### 파스칼의 삼각형")
        # HTML로 중앙 정렬된 삼각형 표시
        html_content = '<div style="text-align: center; font-family: monospace; line-height: 1.8;">'
        for i, row in enumerate(pascal):
            # 들여쓰기
            indent = "&nbsp;" * (2 * (rows - i - 1))
            row_str = " &nbsp; ".join(str(x) for x in row)
            html_content += f"{indent}{row_str}<br>"
        html_content += "</div>"
        st.markdown(html_content, unsafe_allow_html=True)
    else:
        st.markdown("#### 파스칼의 삼각형 (표 형식)")
        # 표 형식으로 표시
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("**행(n)**")
            for i in range(rows):
                st.write(f"{i}")
        with col2:
            st.markdown("**값**")
            for row in pascal:
                st.write(str(row))
    
    st.markdown("---")
    
    st.subheader("파스칼의 삼각형의 성질")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**각 행의 합:**")
        for i, row in enumerate(pascal):
            row_sum = sum(row)
            st.write(f"행 {i}: {row_sum} = 2^{i}")
    
    with col2:
        st.markdown("**대각선 (n 선택 1):**")
        for i in range(min(rows, 8)):
            st.write(f"행 {i}: C({i},1) = {i}")
    
    with col3:
        st.markdown("**중앙값 (n이 홀수일 때):**")
        for i, row in enumerate(pascal):
            if len(row) % 2 == 1:
                center = row[len(row) // 2]
                st.write(f"행 {i}: 중앙값 = {center}")

with tab2:
    st.subheader("이항정리와 파스칼의 삼각형의 관계")
    
    st.markdown("""
    이항정리에서 나타나는 **이항계수**가 정확히 파스칼의 삼각형의 각 요소입니다!
    """)
    
    st.markdown("---")
    
    st.markdown("#### 이항정리의 일반식")
    st.latex(r"(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^{k}")
    
    st.markdown("여기서 이항계수는:")
    st.latex(r"\binom{n}{k} = \frac{n!}{k!(n-k)!}")
    
    st.markdown("---")
    
    st.markdown("#### 예시: (a+b)^5 의 계수")
    
    # 5행 파스칼의 삼각형
    pascal_5 = generate_pascal_triangle(6)
    n = 5
    row = pascal_5[n]
    
    st.latex(f"(a+b)^5 = {row[0]}a^5 + {row[1]}a^4b + {row[2]}a^3b^2 + {row[3]}a^2b^3 + {row[4]}ab^4 + {row[5]}b^5")
    
    st.markdown("**이항계수 계산:**")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    positions = [
        (col1, 5, 0),
        (col2, 5, 1),
        (col3, 5, 2),
        (col4, 5, 3),
        (col5, 5, 4),
        (col6, 5, 5),
    ]
    
    for col, n_val, k_val in positions:
        with col:
            coeff = math.comb(n_val, k_val)
            st.markdown(f"**C({n_val},{k_val})**")
            st.latex(f"\\binom{{{n_val}}}{{{k_val}}} = {coeff}")
    
    st.markdown("---")
    
    st.markdown("#### 파스칼의 삼각형에서 읽기")
    
    n_select = st.slider("n 선택:", min_value=0, max_value=10, value=5)
    pascal_large = generate_pascal_triangle(n_select + 1)
    row_selected = pascal_large[n_select]
    
    st.markdown(f"**n = {n_select}일 때의 파스칼의 삼각형 {n_select}행:**")
    st.write(f"🔹 {row_selected}")
    
    st.markdown(f"**이는 (a+b)^{n_select}의 모든 계수입니다:**")
    
    expansion_terms = []
    for k in range(n_select + 1):
        coeff = row_selected[k]
        power_a = n_select - k
        power_b = k
        
        if power_a == 0:
            expansion_terms.append(f"{coeff}b^{power_b}")
        elif power_b == 0:
            expansion_terms.append(f"{coeff}a^{power_a}")
        else:
            expansion_terms.append(f"{coeff}a^{power_a}b^{power_b}")
    
    expansion = " + ".join(expansion_terms)
    st.success(f"(a+b)^{n_select} = {expansion}")
    
    st.markdown("---")
    
    st.markdown("#### 파스칼의 삼각형의 구성 원리")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**인접한 두 수의 합:**")
        st.image("data:image/svg+xml,%3Csvg width='200' height='150' xmlns='http://www.w3.org/2000/svg'%3E%3Ctext x='50' y='30' font-size='18' font-weight='bold'%3E1%3C/text%3E%3Ctext x='100' y='30' font-size='18' font-weight='bold'%3E1%3C/text%3E%3Ctext x='75' y='70' font-size='18' font-weight='bold' fill='red'%3E2%3C/text%3E%3Ctext x='20' y='120' font-size='14'%3E1+1=2%3C/text%3E%3C/svg%3E", use_column_width=True)
        st.latex(r"\text{새로운 값} = \text{위-왼쪽} + \text{위-오른쪽}")
    
    with col2:
        st.markdown("**예: 4행의 예시**")
        st.code("""
    행 2:        1  1  1
    행 3:      1  2  2  1
    
    2 = 1+1
    2 = 1+1
        """)
    
    st.markdown("---")
    
    st.info("""
    💡 **핵심 정리:**
    - **파스칼의 삼각형의 (n,k) 위치의 값 = C(n,k)** (이항계수)
    - **(a+b)^n을 전개할 때의 모든 계수 = n행의 파스칼의 삼각형**
    - **각 행의 합 = 2^n**
    """)
