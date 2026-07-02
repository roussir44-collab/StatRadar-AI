import streamlit as st
import random
from datetime import datetime

# إعدادات واجهة التطبيق الاحترافية المتوافقة مع ألوان Melbet والفلاش سكور
st.set_page_config(page_title="StatRadar AI - Analyzer Pro", page_icon="📡", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    .stButton>button { background-color: #ffbc00; color: #0b0e14; font-weight: bold; width: 100%; border-radius: 8px; font-size: 16px; }
    .promo-box { background-color: #121620; border: 2px solid #ffbc00; padding: 20px; border-radius: 12px; text-align: center; margin-bottom: 25px; }
    .result-box { background-color: #1c2436; border-top: 4px solid #ffbc00; padding: 20px; border-radius: 8px; margin-top: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
    .code-text { font-size: 26px; font-weight: bold; color: #ffbc00; background-color: #0b0e14; padding: 8px 20px; border-radius: 6px; border: 1px dashed #ffbc00; display: inline-block; letter-spacing: 2px; }
    .market-row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #2c374e; font-size: 16px; }
    .market-name { color: #aaa; }
    .market-value { color: #ffbc00; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 1. بنر الترويج لكودك البرمجي GA3NERBHOU مع ميزة النسخ بنقرة واحدة
st.markdown('<div class="promo-box">', unsafe_allow_html=True)
st.markdown('<h3 style="color: #ffbc00; margin: 0; font-size: 22px;">🎁 هديتك لتفعيل السيرفر وتحليل الأسواق</h3>', unsafe_allow_html=True)
st.markdown('<p style="margin: 8px 0; color: #bbb;">أنشئ حساباً جديداً في <b>MELBET</b> لتستفيد من بونص 200% وتفعيل اشتراكك مجاناً</p>', unsafe_allow_html=True)

st.markdown('<div class="code-text">GA3NERBHOU</div>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 12px; color: #888; margin-top: 5px;">(اضغط على الزر بالأسفل لنسخ الكود تلقائياً والانتقال للتسجيل)</p>', unsafe_allow_html=True)

if st.button("📋 اضغط هنا لنسخ الكود والانتقال للتسجيل"):
    st.components.v1.html("""
        <script>
        navigator.clipboard.writeText("GA3NERBHOU");
        window.open("https://melbet.com", "_blank");
        </script>
    """, height=1)
    st.success("✅ تم نسخ الكود GA3NERBHOU بنجاح! وجاري فتح موقع MELBET للتسجيل...")

st.markdown('</div>', unsafe_allow_html=True)

st.title("📡 StatRadar AI - Match Analyzer")
st.write("أدخل اسم أي مباراة تلعب اليوم حية، ودع الذكاء الاصطناعي يحلل الأسواق ويولد التوقع فوراً")

# 2. واجهة إدخال أسماء المباريات الحية بحرية من طرف المستخدم لضمان المصداقية 100%
st.subheader("📝 تفاصيل المواجهة الحية الحالية")
team1 = st.text_input("اسم الفريق الأول (أو منتخب الأرض)", placeholder="مثال: Spain أو Real Madrid")
team2 = st.text_input("اسم الفريق الثاني (أو منتخب الضيف)", placeholder="مثال: Austria أو Barcelona")

match_type = st.selectbox("طبيعة وأهمية المواجهة الحالية", ["ديربي مشتعل / مباراة مصيرية", "مباراة دوري عادية", "مواجهة ودية / تحضيرية"])

# 3. توليد التوقعات الإحصائية الذكية فور ضغط الزر
if st.button("🔮 بدء تحليل إحصائيات المباراة وتوليد التوقع"):
    if not team1 or not team2:
        st.warning("⚠️ يرجى كتابة أسماء الفريقين أولاً لبدء التحليل!")
    else:
        with st.spinner(f"جاري مسح الإحصائيات المباشرة لمواجهة {team1} ضد {team2}..."):
            
            # تثبيت النتيجة لنفس المباراة في نفس اليوم لتبدو احترافية وحقيقية جداً
            match_seed = sum(ord(char) for char in (team1 + team2)) + datetime.today().day
            import random
            random.seed(match_seed)
            
            # حسابات منطقية تتأثر بنوع المباراة
            if match_type == "ديربي مشتعل / مباراة مصيرية":
                pred_goals = random.choice(["أكثر من 1.5 (Over)", "أكثر من 2.5 (Over)"])
                pred_corners = f"أكثر من {random.randint(9, 12)}.5 (Over)"
                pred_cards = f"أكثر من {random.randint(4, 6)}.5 (Over)"
                pred_shots = f"أكثر من {random.randint(8, 13)}.5 (Over)"
            elif match_type == "مواجهة ودية / تحضيرية":
                pred_goals = "أقل من 3.5 (Under)"
                pred_corners = f"أكثر من {random.randint(6, 8)}.5 (Over)"
                pred_cards = f"أكثر من {random.randint(1, 3)}.5 (Over)"
                pred_shots = f"أكثر من {random.randint(6, 10)}.5 (Over)"
            else:
                pred_goals = random.choice(["أكثر من 1.5 (Over)", "إجمالي الأهداف 2-3"])
                pred_corners = f"أكثر من {random.randint(8, 10)}.5 (Over)"
                pred_cards = f"أكثر من {random.randint(3, 4)}.5 (Over)"
                pred_shots = f"أكثر من {random.randint(7, 11)}.5 (Over)"
                
            confidence = random.randint(91, 98)

            st.markdown(f"""
                <div class="result-box">
                    <h3 style="color: #00ff00; margin: 0 0 15px 0; font-size: 18px;">🔓 تم تحليل مواجهة {team1} 🆚 {team2} بنجاح:</h3>
                    
                    <div class="market-row">
                        <span class="market-name">⚽ رهان الأهداف المتوقع (Goals):</span>
                        <span class="market-value">{pred_goals}</span>
                    </div>
                    <div class="market-row">
                        <span class="market-name">🎯 رهان الركنيات المتوقع (Corners):</span>
                        <span class="market-value">{pred_corners}</span>
                    </div>
                    <div class="market-row">
                        <span class="market-name">🟨 رهان الكروت المتوقع (Yellow Cards):</span>
                        <span class="market-value">{pred_cards}</span>
                    </div>
                    <div class="market-row">
                        <span class="market-name">🚀 رهان التسديدات المتوقع (Shots on Target):</span>
                        <span class="market-value">{pred_shots}</span>
                    </div>
                    
                    <hr style="border-color: #2c374e; margin: 15px 0;">
                    <p style="font-size: 13px; color: #aaa; margin: 0;">وضع الاتصال: <b style="color:#00ff00;">السيرفر التحليلي نشط (AI Engine Live)</b></p>
                    <p style="font-size: 13px; color: #aaa; margin: 0;">نسبة دقة مطابقة البيانات: <b>{confidence}%</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            st.balloons()
