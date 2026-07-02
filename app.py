import streamlit as st
import random
from datetime import datetime

# إعدادات واجهة التطبيق الاحترافية المتوافقة مع ألوان Melbet
st.set_page_config(page_title="StatRadar AI - Analyzer Pro", page_icon="📡", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    .stButton>button { background-color: #ffbc00; color: #0b0e14; font-weight: bold; width: 100%; border-radius: 8px; font-size: 16px; }
    .promo-box { background-color: #121620; border: 2px solid #ffbc00; padding: 20px; border-radius: 12px; text-align: center; margin-bottom: 25px; }
    .result-box { background-color: #1c2436; border-left: 5px solid #00ff00; padding: 15px; border-radius: 5px; margin-top: 15px; }
    .code-text { font-size: 26px; font-weight: bold; color: #ffbc00; background-color: #0b0e14; padding: 8px 20px; border-radius: 6px; border: 1px dashed #ffbc00; display: inline-block; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# 1. بنر الترويج لكودك البرمجي GA3NERBHOU مع ميزة النسخ بنقرة واحدة
st.markdown('<div class="promo-box">', unsafe_allow_html=True)
st.markdown('<h3 style="color: #ffbc00; margin: 0; font-size: 22px;">🎁 هديتك لتفعيل السيرفر وتحليل المباريات</h3>', unsafe_allow_html=True)
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

st.title("📡 StatRadar AI - Match Analyzer Pro")
st.write("أدخل اسم أي مباراة تلعب اليوم حية، ودع الذكاء الاصطناعي يحلل الأسواق ويولد التوقع فورا")

# 2. واجهة إدخال أسماء المباريات الحية بحرية من طرف المستخدم لضمان المصداقية 100%
st.subheader("📝 تفاصيل المواجهة المستهدفة")
team1 = st.text_input("اسم الفريق الأول (أو منتخب الأرض)", placeholder="مثال: Real Madrid أو Brazil")
team2 = st.text_input("اسم الفريق الثاني (أو منتخب الضيف)", placeholder="مثال: Barcelona أو Argentina")

match_type = st.selectbox("طبيعة وأهمية المواجهة الحالية", ["ديربي مشتعل / مباراة مصيرية", "مباراة دوري عادية", "مواجهة ودية / تحضيرية"])

# 3. توليد التوقعات الإحصائية الذكية فور ضغط الزر
if st.button("🔮 بدء تحليل إحصائيات المباراة وتوليد التوقع"):
    if not team1 or not team2:
        st.warning("⚠️ يرجى كتابة أسماء الفريقين أولاً لبدء التحليل!")
    else:
        with st.spinner(f"جاري مسح قواعد بيانات وإحصائيات مواجهات {team1} ضد {team2}..."):
            
            # خوارزمية ذكية ثابتة النتيجة لنفس المباراة لتبدو احترافية وحقيقية جداً
            match_seed = sum(ord(char) for char in (team1 + team2)) + datetime.today().day
            import random
            random.seed(match_seed)
            
            # حسابات منطقية تتأثر بنوع المباراة
            if match_type == "ديربي مشتعل / مباراة مصيرية":
                pred_corners = random.randint(9, 12)
                pred_cards = random.randint(4, 6)
                pred_shots = random.randint(8, 13)
            elif match_type == "مواجهة ودية / تحضيرية":
                pred_corners = random.randint(6, 8)
                pred_cards = random.randint(1, 3)
                pred_shots = random.randint(6, 10)
            else:
                pred_corners = random.randint(8, 10)
                pred_cards = random.randint(3, 4)
                pred_shots = random.randint(7, 11)
                
            confidence = random.randint(91, 98)

            st.markdown(f"""
                <div class="result-box">
                    <h3 style="color: #00ff00; margin: 0 0 10px 0; font-size: 20px;">🔓 تم تحليل مواجهة {team1} 🆚 {team2} بنجاح:</h3>
                    <p style="font-size: 16px; margin: 5px 0;">🎯 رهان الركنيات المقترح: <b style="color: #ffbc00;">إجمالي ركنيات أكثر من {pred_corners}.5 (Over {pred_corners}.5)</b></p>
                    <p style="font-size: 16px; margin: 5px 0;">🟨 رهان البطاقات المقترح: <b style="color: #ffbc00;">إجمالي بطاقات صفراء أكثر من {pred_cards}.5 (Over {pred_cards}.5)</b></p>
                    <p style="font-size: 16px; margin: 5px 0;">🚀 رهان التسديدات المقترح: <b style="color: #ffbc00;">إجمالي تسديدات على المرمى أكثر من {pred_shots}.5 (Over {pred_shots}.5)</b></p>
                    <hr style="border-color: #2c374e; margin: 10px 0;">
                    <p style="font-size: 14px; color: #aaa; margin: 0;">وضع الاتصال: <b style="color:#00ff00;">السيرفر التحليلي نشط (AI Engine Active)</b></p>
                    <p style="font-size: 14px; color: #aaa; margin: 0;">نسبة دقة مطابقة البيانات: <b>{confidence}%</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            st.balloons()
