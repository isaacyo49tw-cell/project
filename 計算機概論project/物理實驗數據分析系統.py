import sympy as sp
import numpy as np

def physics_analyzer_v3():
    print("=== 物理實驗數據分析系統 ===")
    
    # 1. 輸入方程式
    expr_str = input("請輸入方程式 (π請打pi, e請打exp(1)): ")
    # 定義基礎數學常數，確保最高精度
    math_constants = {
        'pi': sp.pi,
        'e': sp.exp(1)
    }
    
    # 解析方程式
    raw_expr = sp.sympify(expr_str, locals=math_constants)
    
    # 找出所有自由符號，排除 pi 和 e
    all_symbols = [s for s in raw_expr.free_symbols if str(s) not in ['pi', 'E']]
    
    data_values = {}
    data_uncertainties = {}

    print("\n--- 變數數據輸入 ---")
    for sym in all_symbols:
        s_name = str(sym)
        print(f"\n[ 變數: {s_name} ]")
        
        # 輸入量測數據
        raw_data = input(f"請輸入 {s_name} 的數據 (多筆請用空白隔開): ")
        data_list = np.array([float(x) for x in raw_data.split()])
        mean_v = np.mean(data_list)
        
        # 詢問不確定度
        unc_input = input(f"請輸入 {s_name} 的器具精度 (若是已知物理常數請輸入 'c' 或 '0'): ")
        
        if unc_input.lower() == 'c' or float(unc_input) == 0:
            u_c = 0
            print(f"-> {s_name} 已被標記為常數，不計入不確定度傳遞。")
        else:
            u_b = float(unc_input)
            # 計算 A 類不確定度
            u_a = np.std(data_list, ddof=1) / np.sqrt(len(data_list)) if len(data_list) > 1 else 0
            u_c = np.sqrt(u_a**2 + u_b**2)
            print(f"-> 平均值: {mean_v:.6f}, 合成不確定度: {u_c:.6f}")

        data_values[sym] = mean_v
        data_uncertainties[sym] = u_c

    # 2. 計算最佳值
    # evalf(50) 可以指定計算到小數點後 50 位，保證精度
    best_value = raw_expr.subs(data_values).evalf()
    
    # 3. 誤差傳遞 (偏微分)
    variance_terms = []
    for sym in all_symbols:
        if data_uncertainties[sym] > 0:
            # 只對有誤差的變數求偏微分
            partial_diff = sp.diff(raw_expr, sym)
            term = (partial_diff.subs(data_values).evalf() * data_uncertainties[sym])**2
            variance_terms.append(term)
    
    total_u = sp.sqrt(sum(variance_terms)).evalf()

    print("\n" + "="*50)
    print(f"解析方程式: {raw_expr}")
    print(f"計算結果 (Best Value): {best_value}")
    print(f"總不確定度 (Uncertainty): {total_u}")
    print(f"\n標準表示法: {best_value:.6f} ± {total_u:.6f}")
    print("="*50)

if __name__ == "__main__":
    physics_analyzer_v3()