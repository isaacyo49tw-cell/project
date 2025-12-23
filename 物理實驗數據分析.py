import sympy as sp
import numpy as np

def analyze_experiment():
    print("=== 通用物理實驗數據分析工具 ===")
    
    # 1. 輸入方程式
    expr_str = input("請輸入方程式 (例如: 4 * pi**2 * L / T**2): ")
    
    # 2. 定義符號 (包含常數 pi)
    # 我們將方程式中的字母找出來當作變數
    potential_vars = sp.sympify(expr_str).free_symbols
    var_names = [str(v) for v in potential_vars ]
    
    # 建立 SymPy 符號物件
    symbols_dict = {name: sp.Symbol(name) for name in var_names}
    
    # 解析方程式
    formula = sp.sympify(expr_str)
    
    # 3. 輸入實驗數據與精度
    values_map = {}
    uncertainties_map = {}
    
    print("\n--- 請輸入數據與儀器精度 ---")
    for name in var_names:
        val = input(f"請輸入 {name} 的多組量測數據(以空白間隔開): ")
        data_list=np.array([float(x) for x in val.split()])
        mean_val = np.mean(data_list)
        unc = float(input(f"請輸入 {name} 儀器最小刻度(若為物理常數，輸入C或0): "))
        if unc==0 or unc=='C'or unc=='c':
            u_c=0
        else:
            n=len(data_list)
            u_b=unc/np.sqrt(12)
            if n > 1:
                # 樣本標準差 s
                s = np.std(data_list, ddof=1)
                # A 類不確定度 u_a = s / sqrt(n)
                u_a = s / np.sqrt(n)
            else:
                u_a = 0
                print("注意：僅有一組數據，A 類不確定度設為 0")
            u_c=np.sqrt(u_a**2+u_b**2)
        values_map[symbols_dict[name]] = mean_val
        uncertainties_map[symbols_dict[name]] = u_c

    # 4. 計算最佳值 (Best Value)
    # 將 pi 替換為數值，並帶入量測值
    best_value = formula.subs(values_map).evalf()
    
    # 5. 自動推導不確定度傳遞 (Uncertainty Propagation)
    # 公式: Delta_f = sqrt( sum( (df/dx_i * Delta_x_i)^2 ) )
    variance_terms = []
    for var_symbol in values_map.keys():
        # 對該變數求偏微分
        partial_diff = sp.diff(formula, var_symbol)
        # 帶入數值計算該項的貢獻
        term = (partial_diff.subs(values_map).evalf() * uncertainties_map[var_symbol])**2
        variance_terms.append(term)
    
    total_uncertainty = sp.sqrt(sum(variance_terms)).evalf()

    # 6. 輸出結果
    print("\n--- 分析結果 ---")
    print(f"使用的方程式: {formula}")
    print(f"計算之最佳值: {best_value:.6f}")
    print(f"合成不確定度: {total_uncertainty:.6f}")
    print(f"最終結果表示: {best_value:.6f} ± {total_uncertainty:.6f}")

if __name__ == "__main__":
    analyze_experiment()