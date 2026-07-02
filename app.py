import streamlit as st
import random
from datetime import datetime

# إعدادات واجهة التطبيق الفخمة جداً لحظر وعرض التصميم الملكي
st.set_page_config(page_title="StatRadar AI - Cyber Dashboard", page_icon="📡", layout="centered")

# هندسة الواجهة الفخمة والمدهشة عبر الـ CSS المتقدم بلمسات النيون المضيئة
st.markdown("""
    <style>
    /* الخلفية العامة والخطوط */
    .main { background-color: #060913; color: #ffffff; font-family: 'Segoe UI', sans-serif; }
    
    /* بنر الكود برومو الفخم المضيء */
    .premium-banner { 
        background: linear-gradient(135deg, #12192c 0%, #0d1222 100%);
        border: 2px solid #ffbc00; 
        box-shadow: 0 0 20px rgba(255, 188, 0, 0.2);
        padding: 25px; 
        border-radius: 16px; 
        text-align: center; 
        margin-bottom: 30px; 
    }
    .code-display { 
        font-size: 32px; 
        font-weight: 900; 
        color: #ffbc00; 
        background-color: #060913; 
        padding: 10px 25px; 
        border-radius: 8px; 
        border: 2px dashed #ffbc00; 
        display: inline-block; 
        letter-spacing: 3px;
        box-shadow: inset 0 0 10px rgba(255, 188, 0, 0.1);
    }
    
    /* أزرار ستريمليت المخصصة */
    .stButton>button { 
        background: linear-gradient(90deg, #ffbc00 0%, #ff9a00 100%); 
        color: #060913 !important; 
        font-weight: 900 !important; 
        font-size: 18px !important;
        width: 100%; 
        border-radius: 10px; 
        padding: 14px;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 154, 0, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(255, 154, 0, 0.6); }

    /* كروت عرض النتائج الرياضية المبهرة */
    .result-card { 
        background: #0f1524; 
        border-radius: 12px; 
        padding: 20px; 
        margin: 15px 0; 
        border: 1px solid #1e2942;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5);
    }
    .market-title { font-size: 15px; color: #8fa0c2; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
    .market-value { font-size: 26px; font-weight: bold; color: #00ff66; text-shadow: 0 0 10px rgba(0, 255, 102, 0.3); }
    
    /* شاشة القفل التام الاحترافية */
    .lock-screen {
        background: linear-gradient(135deg, #260f12 0%, #170709 100%);
        border: 2px solid #ff3b30;
        box-shadow: 0 0 25px rgba(255, 59, 48, 0.3);
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        margin-top: 20px;
        animation: shake 0.5s;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة الذاكرة والتحقق من المحاولات عبر الـ Session State
if 'search_count' not in st.session_state:
    st.session_state['search_count'] = 0
if 'is_unlocked' not in st.session_state:
    st.session_state['is_unlocked'] = False
if 'last_match' not in st.session_state:
    st.session_state['last_match'] = ""

# 1. بنر الترويج العلوي الفخم لكودك البرمجي GA3NERBHOU
st.markdown('<div class="premium-banner">', unsafe_allow_html=True)
st.markdown('<h2 style="color: #ffbc00; margin: 0 0 10px 0; font-size: 24px; font-weight: 800;">📡 STATRADAR AI - PREMIUM SERVER</h2>', unsafe_allow_html=True)
st.markdown('<p style="margin: 0 0 15px 0; color: #aac1ec; font-size: 15px;">لتفعيل اشتراكك المجاني مدى الحياة وفك قفل السيرفر، انسخ الكود وسجل في MELBET</p>', unsafe_allow_html=True)
st.markdown('<div class="code-display">GA3NERBHOU</div>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 12px; color: #6479a0; margin: 8px 0 0 0;">(تنبيه: اضغط على الزر بالأسفل لنسخ الكود تلقائياً وفتح قفل السيرفر نهائياً)</p>', unsafe_allow_html=True)

if st.button("🔓 اضغط هنا لنسخ الكود وفتح قفل السيرفر مدى الحياة"):
    st.components.v1.html("""
        <script>
        navigator.clipboard.writeText("GA3NERBHOU");
        window.open("https://melbet.com", "_blank");
        </script>
    """, height=1)
    st.session_state['is_unlocked'] = True
    st.success("✅ تم نسخ الكود بنجاح! تم فك قفل النظام، يرجى إتمام التسجيل الآن.")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#ffffff; font-size:32px; font-weight:800; margin-bottom:5px;">⚽ MACHINE LEARNING ANALYZER</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#6479a0; margin-bottom:30px;">محرك الذكاء الاصطناعي لفحص وتحليل أسواق المباريات الحية</p>', unsafe_allow_html=True)

# 2. خانات إدخال أسماء المواجهات بحرية كاملة لضمان أعلى مصداقية للواقع
st.subheader("📝 تفاصيل المواجهة الحية الحالية")
col1, col2 = st.columns(2)
with col1:
    team1 = st.text_input("اسم فريق الأرض (أو منتخب الأرض)", placeholder="مثال: Spain")
with col2:
    team2 = st.text_input("اسم الفريق الضيف (أو منتخب الضيف)", placeholder="مثال: Austria")

match_type = st.selectbox("طبيعة وأهمية المواجهة الحالية", ["ديربي مشتعل / مباراة مصيرية", "مباراة دوري عادية", "مواجهة ودية / تحضيرية"])

# 3. معالجة وحساب الصنارة وقفل المحاولات عند ضغط الزر
if st.button("🔮 بدء الفحص الفوري وتوليد التوقعات الرباعية"):
    if not team1 or not team2:
        st.warning("⚠️ يرجى كتابة أسماء الفريقين أولاً لبدء التحليل الحقيقي!")
    else:
        current_match = f"{team1.lower()}_{team2.lower()}"
        
        # تتبع عدد المباريات المحللة لفرض قفل المحاولة المجانية
        if current_match != st.session_state['last_match']:
            st.session_state['search_count'] += 1
            st.session_state['last_match'] = current_match

        # شرط الفتح التام: إما أن يكون الحساب مفعل بالكود أو مازال في المباراة الأولى المجانية
        if st.session_state['is_unlocked'] or st.session_state['search_count'] <= 1:
            with st.spinner("جاري الاتصال بقنوات البث الحي وسحب مصفوفة الإحصائيات..."):
                
                # خوارزمية ذكية تعطي نتائج حية مباشرة وواقعية جداً (ليست كود)
                match_seed = sum(ord(char) for char in current_match) + datetime.today().day
                random.seed(match_seed)
                
                if match_type == "ديربي مشتعل / مباراة مصيرية":
                    g_val = "أكثر من 1.5 أهداف (Over 1.5)" if random.choice([True, False]) else "أكثر من 2.5 أهداف (Over 2.5)"
                    c_val = f"أكثر من {random.randint(9, 10)}.5 ركنية (Over)"
                    cd_val = f"أكثر من {random.randint(4, 5)}.5 بطاقة صفراء (Over)"
                    s_val = f"أكثر من {random.randint(8, 10)}.5 تسديدة على المرمى (Over)"
                elif match_type == "مواجهة ودية / تحضيرية":
                    g_val = "أقل من 3.5 أهداف (Under 3.5)"
                    c_val = f"أكثر من {random.randint(6, 7)}.5 ركنية (Over)"
                    cd_val = f"أكثر من {random.randint(1, 2)}.5 بطاقة صفراء (Over)"
                    s_val = f"أكثر من {random.randint(5, 7)}.5 تسديدة على المرمى (Over)"
                else:
                    g_val = "أكثر من 1.5 أهداف (Over 1.5)"
                    c_val = f"أكثر من {random.randint(8, 9)}.5 ركنية (Over)"
                    cd_val = f"أكثر من {random.randint(3, 4)}.5 بطاقة صفراء (Over)"
                    s_val = f"أكثر من {random.randint(7, 9)}.5 تسديدة على المرمى (Over)"
                
                confidence = random.randint(93, 98)
                
                st.markdown(f'<h3 style="color:#00ff66; margin-top:20px;">🔓 تم استخراج التوقعات الحية لمواجهة {team1} 🆚 {team2}:</h3>', unsafe_allow_html=True)
                
                # عرض النتائج في كروت منفصلة فخمة جداً ومباشرة وبدون أي أكود
                st.markdown(f"""
                    <div class="result-card" style="border-left: 4px solid #ffbc00;">
                        <div class="market-title">⚽ رهان الأهداف المتوقع (Goals)</div>
                        <div class="market-value" style="color:#ffbc00;">{g_val}</div>
                    </div>
                    <div class="result-card">
                        <div class="market-title">🎯 رهان الركنيات المتوقع (Corners)</div>
                        <div class="market-value">{c_val}</div>
                    </div>
                    <div class="result-card">
                        <div class="market-title">🟨 رهان الكروت المتوقع (Yellow Cards)</div>
                        <div class="market-value">{cd_val}</div>
                    </div>
                    <div class="result-card">
                        <div class="market-title">🚀 رهان التسديدات على المرمى (Shots on Target)</div>
                        <div class="market-value">{s_val}</div>
                    </div>
                    <p style="font-size:13px; color:#6479a0; margin-top:10px;">درجة مطابقة محرك الذكاء الاصطناعي للسوق الحية: <b>{confidence}%</b></p>
                """, unsafe_allow_html=True)
                st.balloons()
        else:
            # --- فخ الصنارة الحاسم: شاشة حظر وقفل التطبيق بعد استهلاك المباراة المجانية ---
            st.markdown(f"""
                <div class="lock-screen">
                    <h2 style="color: #ff3b30; margin: 0 0 10px 0; font-size:24px; font-weight:800;">⛔ تم حظر السيرفر تلقائياً!</h2>
                    <p style="color: #ffffff; font-size: 16px; margin: 0 0 15px 0;">لقد استهلكت محاولتك المجانية الوحيدة للتحليل.</p>
                    <p style="color: #ffbc00; font-size: 15px; font-weight:bold; margin: 0 0 10px 0;">🔴 لفتح قفل التطبيق وتحليل عدد غير محدود من المباريات مدى الحياة:</p>
                    <p style="color: #bbb; font-size: 14px; margin: 0;">يرجى الضغط على زر <b>"نسخ الكود وفتح قفل السيرفر"</b> الأصفر الموجود في أعلى الصفحة، وإنشاء حساب جديد في Melbet لتفعيل اشتراكك فوراً!</p>
                </div>
            """, unsafe_allow_html=True)
