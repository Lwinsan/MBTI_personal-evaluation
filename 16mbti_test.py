import streamlit as st
import csv

from sklearn.neighbors import KNeighborsClassifier
import joblib

##########
# Set background image
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('mj_01.png')   


######....
#for test cases 
with st.sidebar:
    st.title(":red[Model Test case!]")
    st.write("This section aim for testing the modle!")

    # Create six input boxes for 10 digits each
    digits1 = st.text_input("Questions 1-10", value="0,0,0,0,0,0,0,0,0,0")
    digits2 = st.text_input("Questions 11-20", value="0,0,0,0,0,0,0,0,0,0")
    digits3 = st.text_input("Questions 21-30", value="0,0,0,0,0,0,0,0,0,0")
    digits4 = st.text_input("Questions 31-40", value="0,0,0,0,0,0,0,0,0,0")
    digits5 = st.text_input("Questions 41-50", value="0,0,0,0,0,0,0,0,0,0")
    digits6 = st.text_input("Questions 51-60", value="0,0,0,0,0,0,0,0,0,0")

    # Create a submit button
    # Create a submit button
    if st.button("Test"):
        # Combine the inputs into a single list
        digit_list = [digits1, digits2, digits3, digits4, digits5, digits6]
        digit_str = ",".join(digit_list) # Combine the list of strings into a single string with "," as separator
        digit_list = []
        for digit in digit_str.split(","):
            if digit.strip(): # Check if the input is not empty
                digit_list.append(int(digit))
    
    ####..........................
    
    
        #prediction
        # Load the KNN model from the saved file
        knn_model = joblib.load('knn_model.sav')


        # Define a function to make predictions using the KNN model
        def predict_type(input_data):
            input_data = [input_data]
            prediction = knn_model.predict(input_data)
            return prediction[0]

        # Create a Streamlit app
        st.subheader(":violet[Type Prediction]")
        
        if digit_list == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
            st.write(":red[Abnormal Answer!]")
        else:
            # Get user input and make predictions
            prediction = predict_type(digit_list)
            # Show the predicted Type
            st.write(f"Predicted Type: {prediction}")
    
        
    st.subheader(":violet[..............*****..............]")
    st.subheader(" ")
    st.subheader(" ")
######....





st.title(":green[Personality Evaluation!]")
st.caption(':blue[အင်္ဂလိပ်လို နားမရှင်းရင် ရမ်းသမ်းပြန်ထားတဲ့ မြန်မာလိုဖတ်ပါ အဲ့လို့မှ နားမရှင်းသေးရင် ထင်ရာသာရွေးလိုက်ပါ😜]')


with st.sidebar:
    st.header(":violet[Note...!]")
    st.subheader(":violet[Term for 16 MBTI]")
    st.write("\n- Extraversion (E) \n- Introversion (I) \n- Sensing (S) \n- Intuition (N) \n- Thinking (T) \n- Feeling (F) \n- Judging (J) \n- Perceiving (P)")
    st.subheader(":violet[List of 16 MBTI]")
    st.write("\n- ISTJ - The Inspector \n- ISFJ - The Protector \n- INFJ - The Counselor \n- INTJ - The Mastermind \n- ISTP - The Craftsman \n- ISFP - The Composer \n- INFP - The Healer \n- INTP - The Architect \n- ESTP - The Dynamo \n- ESFP - The Performer \n- ENFP - The Champion \n- ENTP - The Visionary \n- ESTJ - The Supervisor \n- ESFJ - The Provider \n- ENFJ - The Teacher \n- ENTJ - The Commander")

    




# Define the questions
eng_questions = [
    'You regularly make new friends.',
    'You spend a lot of your free time exploring various random topics that pique your interest.',
    'Seeing other people cry can easily make you feel like you want to cry too.',
    'You often make a backup plan for a backup plan.',
    'You usually stay calm, even under a lot of pressure.',
    'At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know.',
    'You prefer to completely finish one project before starting another.',
    'You are very sentimental.',
    'You like to use organizing tools like schedules and lists.',
    'Even a small mistake can cause you to doubt your overall abilities and knowledge.',
    'You feel comfortable just walking up to someone you find interesting and striking up a conversation.',
    'You are not too interested in discussing various interpretations and analyses of creative works.',
    'You are more inclined to follow your head than your heart.',
    'You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.',
    'You rarely worry about whether you make a good impression on people you meet.',
    'You enjoy participating in group activities.',
    'You like books and movies that make you come up with your own interpretation of the ending.',
    'Your happiness comes more from helping others accomplish things than your own accomplishments.',
    'You are interested in so many things that you find it difficult to choose what to try next.',
    'You are prone to worrying that things will take a turn for the worse.',
    'You avoid leadership roles in group settings.',
    'You are definitely not an artistic type of person.',
    'You think the world would be a better place if people relied more on rationality and less on their feelings.',
    'You prefer to do your chores before allowing yourself to relax.',
    'You enjoy watching people argue.',
    'You tend to avoid drawing attention to yourself.',
    'Your mood can change very quickly.',
    'You lose patience with people who are not as efficient as you.',
    'You often end up doing things at the last possible moment.',
    'You have always been fascinated by the question of what, if anything, happens after death.',
    'You usually prefer to be around others rather than on your own.',
    'You become bored or lose interest when the discussion gets highly theoretical.',
    'You find it easy to empathize with a person whose experiences are very different from yours.',
    'You usually postpone finalizing decisions for as long as possible.',
    'You rarely second-guess the choices that you have made.',
    'After a long and exhausting week, a lively social event is just what you need.',
    'You enjoy going to art museums.',
    'You often have a hard time understanding other people’s feelings.',
    'You like to have a to-do list for each day.',
    'You rarely feel insecure.',
    'You avoid making phone calls.',
    'You often spend a lot of time trying to understand views that are very different from your own.',
    'In your social circle, you are often the one who contacts your friends and initiates activities.',
    'If your plans are interrupted, your top priority is to get back on track as soon as possible.',
    'You are still bothered by mistakes that you made a long time ago.',
    'You rarely contemplate the reasons for human existence or the meaning of life.',
    'Your emotions control you more than you control them.',
    'You take great care not to make people look bad, even when it is completely their fault.',
    'Your personal work style is closer to spontaneous bursts of energy than organized and consistent efforts.',
    'When someone thinks highly of you, you wonder how long it will take them to feel disappointed in you.',
    'You would love a job that requires you to work alone most of the time.',
    'You believe that pondering abstract philosophical questions is a waste of time.',
    'You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.',
    'You know at first glance how someone is feeling.',
    'You often feel overwhelmed.',
    'You complete things methodically without skipping over any steps.',
    'You are very intrigued by things labeled as controversial.',
    'You would pass along a good opportunity if you thought someone else needed it more.',
    'You struggle with deadlines.',
    'You feel confident that things will work out for you.'
]

mm_questions = [
    'သူငယ်ချင်း အသစ်တွေနဲ့ မိတ်ဖွဲ့ရတာသဘောကျတယ်။',
    'အားလပ်ချိန်တွေဆို ရောက်တက်ရာရာ စိတ်ဝင်စားတဲ့ ရာတွေကို စူစမ်းလေ့လာလေ့ရှိတယ်။',
    'အခြားသူတွေ ငိုတာမြင်ရင် သင်လဲ ငိုချင်သလိုခံစားရတယ်။',
    'အလုပ်တခုခု လုပ်တိုင်း အရံအစီစဉ်တွေ အများကြီးစီစဉ် ထားလေ့ရှိတယ်။',
    'သင်ဟာ ဘယ်လိုဖိအားမျိုးပဲရှိရှိ အေးဆေးတည်ငြိမ်စွာ နေနိုင်တယ်။',
    'လူအများနဲ့ တွေ့ရတဲ့ပွဲတွေတတ်ရင် မသိတဲ့သူတွေကို ကိုယ့်အကြောင်းမိတ်ဆတ်ပြီး စကားပြောတာကို သိပ်လုပ်လေ့ရှိ၊   ။',
    'သင်ဟာ အလုပ်တခုကို ၁၀၀% ပြီးမှ နောက်တခုကိုစချင်တယ်။',
    'သင်ဟာ အရမ်း စိတ်ကူးယဉ်ဆန်တဲ့သူ။',
    'သင်ဟာ အလုပ်တခုခု လုပ်ရင် အချိန်ဇယားတို့ လုပ်ရန်စာရင် မှတ်စု စတဲ့ တစုတစည်းဖော်ပြ ပစ္စည်တွေကို သုံးရတာ နှစ်သက်တယ်။',
    'သင်ဟာ အမှားသေးသေးလေး လုပ်မိရင်တောင် ကိုယ့်ရဲ့ အရည်အချင်းနဲ့ လုပ်နိုင်စွမ်းပေါ်မှာ သံသယဝင်တက်သူ။',
    'စိတ်ဝင်စားစရာကောင်းတဲ့ တစ်စုံတစ်ယောက်ဆီ လျှောက်လှမ်းပြီး စကားစမြည်ပြောရုံနဲ့ အဆင်ပြေတယ်လို့ ခံစားရတယ်။',
    'သင်ဟာ တီထွင်ဖန်တီးမှုတွေလအကြောင်း လေ့လာဆွေးနွေးရတာကို သဘောမကျတဲ့သူ။',
    'သင်ဟာ နှလုံးသားထက် ဦးနှောက်ကို ဦးစားပေးတဲ့သူ။',
    'နေ့စဉ်လုပ်နေကျအတိုင်း လုပ်ရတာထက် လက်ရှိ စိတ်ခံစားချက်ပေါ်မူတည်ပြီး လုပ်ချင်တာလုပ်ရတာကို သဘောကျတဲ့သူ။',
    'သင့်ဟာ သင့်နဲ့တွေတဲ့သူက သင့်ကို အထင်ကြီးပါ့မလားလို့ စိုရိမ်လေ့မရှိဘူး။',
    'သင်ဟာ အဖွဲအစည်းနဲ့ လုပ်ကိုင်ရတာကို သဘောကျတဲ့သူ။',
    'သင်ဟာ အဆုံးသတ်ကို ကြိုတင် ခန့်မှန်းလို့ရတဲ့ ဝတ္ထုတို့ ရုပ်ရှင်တို့ကို ကြိုက်တဲ့သူ။',
    'သင်ဟာ ကိုအောင်မြင်တာထက် တခြားသူတွေကို အောင်မြင်အောင် ကူညီပေးရတာကို ပိုပျော်တဲ့သူ။',
    'သင်ဟာ နောက်တဆင့်တတ်ဖို့ ရွေးချယ်ရခတ်ခဲ့တဲ့ အရာတွေကို လုပ်ရတာစိတ်ဝင်စားတယ်။',
    'သင်ဟာ ကိစ္စတွေ လက်ရှိထက်ပိုဆိုးသွားမှာကို စိုးရိမ်တတ်တဲ့သူ။',
    'သင်ဟာ အဖွဲ့ အစည်းတွေ ခေါင်းဆောင်လုပ်ရမှာကို ရှောင်ရှားတတ်တဲ့သူ။',
    'သင်ဟာ အနုပညာနဲ့ လားလား မှမသတ်ဆိုင်တဲ့သူ။ စိတ်မဝင်စားသူ။',
    'လူတွေဟာ စိတ်ခံစားချက်တွေကို လျှော့ပြီး ဆင်ချင်တုံတရား ပေါ်ဦးစားပေးရင် ကမ္ဘာကြီး ပိုကောင်းလာမယ်လို့ သင်ယုံကြည်တယ်။',
    'နားမယူခင် ကိုယ့်ဝေယျာဝစ္စတွေကို ရင်ပြီးစီးအောင်လုပ်ပီးမှ နားတယ်။',
    'သင်ဟာ လူတွေစကားများ ငြင်းခုံ ရန်ဖြစ်တာကို ကြည့်ရတာသဘောကျတယ်။',
    'သင်ဟာ ကိုယ့်ကိုယ် ကို အာရုံစိုက်လေ့မရှိဘူး။',
    'သင်ဟာ အပြောင်း အလဲမြန်တဲ့သူ။',
    'ကိုယ့်လောက် ကျွမ်းကျွမ်းကျင်ကျင် မလုပ်တတ်တဲ့သူ ကို စိတ်မရှည်ဘူး။',
    'အလုပ်တခုကို သတ်မှတ်ချိန်နောက်ဆုံးရောက်တဲ့အထိ လုပ်နေလေ့ရှိတယ်။',
    'သေပြီးရင် ဘာဖြစ်မလဲ ဆိုတဲ့ မေးခွန်းကို မင်းအမြဲတမ်း စွဲလန်းနေခဲ့တယ်။',
    'မင်းဟာ ကိုယ့်ဘာသာထက် တခြားသူတွေနဲ့ နေရတာ ပိုကြိုက်တယ်။',
    'သင်ဟာ သီအိုရီအရ ဆွေးနွေးမှုလွန်တဲ့အခါ အဲ့အရာပေါ် စိတ်ဝင်စားမှုနဲသွားပြီး ငြီးငွေ့တတ်တဲ့သူ။',
    'သင့်ရဲ့ အတွေ့ကြုံ ကျွမ်းကျင်မှု အရမ်းကွာခြားတဲ့ သူတွေပေါ် စာနာနားလည်ပေးတက်တယ်။',
    'သင်သည် ဆုံးဖြတ်ချက်များ အပြီးသတ်ရန် ဖြစ်နိုင်သမျှကြာအောင် ရွှေ့ဆိုင်းတတ်သည်။',
    'သင်ဟာ ရွေးချယ်ပြီးသား အရာတွေပေါ်မှာ နောက်တခါ ထပ်သုဉ်သတ် တတ်တဲ့သူ။',
    'ရက်သတ္တပတ်အကြာ လောက်ပင်ပမ်းပီးရင် စိတ်အပမ်းဖြေတဲ့ ပွဲတခုခု တတ်သင့်တယ်လို့ထင်တယ်။',
    'နုပညာ ပြတိုက်၊ ပန်ချီ ပြတိုက် သွားရတာ သဘောကျတယ်။',
    'သင်ဟာ တခြားသူတွေရဲ့ ခံစားချက်ကို နားမလည်နိုင်တဲ့သူ။',
    ' သင်ဟာ တနေ့ချင်းစီအတွက် လုပ်စရာ အလုပ်တွေကို ကြိုတင် စာရင်းပြုပြီး လုပ်ရတာကို သဘောကြတယ်။',
    'သင်ကိုယ်သင် မလုံခြုံဘူး အကာကွယ်မဲ့နေတယ်လို့ ခံစာတယ်။',
    'ဖုန်းခေါ်တာကို ရှောင်တယ်။',
    'သင်သည် သင်ကိုယ်ပိုင်အမြင်နှင့် အလွန်ခြားနားသော အမြင်များကို နားလည်ရန် ကြိုးစားဖို့ အချိန်များစွာ ပေးလေ့ရှိသည်။',
    'သင့်ရဲ့ အသိပတ်ဝန်းကျင်မှာ သင်ဟာ အသိမိတ်ဆွေတွေကို သင့်ဘက်ကစပီး ဆတ်သွယ်လေ့ရှိတယ်။',
    'သင်၏ အစီအစဉ်များ ရပ်တန့်သွားပါက၊ သင့်၏ အဓိက ဦးစားပေးမှာ တတ်နိုင်သမျှ အမြန်ဆုံး လမ်းကြောင်းပေါ်သို့ ပြန်လည်ရောက်ရှိရန် ဖြစ်ပါသည်။',
    'သင်ဟာ အတိတ်က အမှားတွေပေါ် တသသ နဲ့ ပူဆွေးတ်တတဲ့သူ။',
    'သင်ဟာ လူ့ရဲ့ ဖြစ်တည်မှုနဲ့ ဘဝရဲ့ အဓိပ္ပါယ်အကြောင်းကို စဉ်းစားလေ့မရှိဘူး။',
    'သင့်ဟာ သင့်ရဲ့ခံစားချက် ကို ထိန်းချုပ်နိုင်တာထက် ခံစားချက်နောက်ကို လိုက်ရတာများတယ်။',
    'သင်ဟာ လူတွေအပြစ်ရှိရင်တောင် အဲ့လူတွေပေါ် အပြစ်မမြင်မိအောင် အထူးကရုစိုက်တယ်။',
    'သင်ရဲ့ အလုပ်လုပ်တဲ့ပုံစံက စနစ်တကျ တသတ်မတ်ထဲ လုပ်တာထက် သူ့အလိုလို ထွက်လာတဲ့ စွမ်းအားတွေ ပေါ်မှီတည်ပီး လုပ်လေ့ရှိတယ်။',
    'တယောက်ယောက်က သင့်ကိုအထင်ကြီးနေပြီဆိုရင်၊ အဲ့ဒိလူက ဘယ်လောက်ကြာရင် ပြန်အထင်သေးသွားမလဲ၊ စိတ်အလိုမကျ ဖြစ်သွားမလဲလို့ တွေးနေလေ့ရှိတယ်။',
    'အလုပ်ချိန် တော်တော်များများမှာ တယာက်ထဲလုပ်ရတဲ့ အလုပ်မျိုးကို သဘောကျတယ်။',
    'အတွေးခေါ်မေးခွန်းများကို အချိန်ယူတွေးနေခြင်းက အလဟာသတ်လအချိန်ဖြုန်ခြင်းလို့ ထင်တယ်။',
    'တိတ်စိတ်ပြီး ရင်းနှီးနေကျ နေရာတွေထက် ယောက်ယက်ခတ် လှုပ်ရှား စည်ကားနေတဲ့ နေရာတွေကို ပိုသဘောကျတယ်။',
    'တစုံ တယောက်ရဲ့ခံစားချက်ကို အကြည့်တချက်နဲ့ တင် နားလည်နိုင်တယ်။',
    'တခါတရံ တခုခုရဲ့ အလွှမ်းမိုးခံနေရတယ်လို့ ခံစားနေတယ်။',
    'အသင်ဟာ အဆင့်မကျော်ပဲ နည်းစနစ်တကျ လုပ်တတ်တယ်။',
    'သင်ဟာ အငြင်းပွါးစရာလို့ သတ်မှတ်ခံထားရတဲ့ အရာတွေကို စိတ်ဝင်စားတယ်။',
    'သင်ဟာ အခွင့်ရေးကောင်းတခု ရရင်တောင် တခြားသူက အဲ့ရာကို သင့်ထက် ပိုလိုအပ်တယ်ဆိုရင် အဲ့အခွင့်ရေးကို လက်လွှတ်ပေးတတ်တယ်။',
    'သင်ဟာ Deadline တွေနဲ့ အလုပ်လုပ်ရတာကို နှစ်သတ်တယ်။',
    'အရာရာ အဆင်ပြေအောင် လုပ်နိုင်တယ်လို့ ကိုယ်ကိုယ်ကို ယုံကြည်တယ်။'
    
]




answer_choices = [
    ("3", "Strongly agree"),
    ("2", "Agree"),
    ("1", "Slightly agree"),
    ("0", "Neither agree nor disagree"),
    ("-1", "Slightly disagree"),
    ("-2", "Disagree"),
    ("-3", "Strongly disagree")
]

# Create a dictionary to store the user's answers
user_answers = {}

# Display each question and allow the user to select an answer

for i, (eng_question, mm_question) in enumerate(zip(eng_questions, mm_questions)):
    key = f"question_{i}"
    #st.write(f"Question {i+1} (Eng): {eng_question}")
    st.write(f"Question {i+1}:")
    st.write(f"(Eng): {eng_question}")
    #st.write(f"Question {i+1} (Myanmar): {mm_question}")
    st.write(f"(Mm): {mm_question}")
    user_answer = st.radio(f"Select your answer for question {i+1}:", answer_choices, key=key)
    
    st.write("..............*****..............")
    user_answers[i] = int(user_answer[0])
    
# Add a submit button to calculate the user's score
if st.button("Submit"):
    # Calculate the user's score as a list of integers
    user_score = [user_answers[i] for i in range(len(user_answers))]
    st.write(f"Your answers: {user_score}")
    
    #prediction
    # Load the KNN model from the saved file
    knn_model = joblib.load('knn_model.sav')


    # Define a function to make predictions using the KNN model
    def predict_type(input_data):
        input_data = [input_data]
        prediction = knn_model.predict(input_data)
        return prediction[0]

    # Create a Streamlit app
    st.subheader(":violet[Type Prediction App]")

    # Get user input and make predictions
    prediction = predict_type(user_score)

    # Show the predicted Type
    #st.write(f"Predicted Type: {prediction}")
    
    if prediction == "ISTJ" :
        st.write("Your type is : :green[ISTJ - The Inspector].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ISTJs are responsible, practical, and detail-oriented individuals who value order, structure, and rules. They tend to be reliable, dependable, and organized, and are often motivated by a sense of duty and responsibility.")
        st.caption("ISTJs များသည် စည်းမျဥ်း၊ ဖွဲ့စည်းပုံနှင့် စည်းကမ်းများကို တန်ဖိုးထားသော တာဝန်ခံမှု၊ လက်တွေ့ကျပြီး အသေးစိတ်ကို ဦးတည်သော ပုဂ္ဂိုလ်များဖြစ်သည်။ ၎င်းတို့သည် ယုံကြည်စိတ်ချရသော၊ အားကိုးအားထားပြုနိုင်သော၊ စည်းစနစ်တကျရှိကြပြီး တာဝန်နှင့် တာဝန်သိစိတ်ဖြင့် လှုံ့ဆော်ပေးလေ့ရှိကြသည်။")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ISTJs tend to be hard-working, loyal, and responsible, and often excel in roles that require attention to detail and a focus on practical outcomes. They may struggle with change or ambiguity and may come across as overly critical or rigid in their thinking.")
        st.caption("ISTJ များသည် အလုပ်ကြိုးစားသူ၊ သစ္စာရှိပြီး တာဝန်သိတတ်ပြီး အသေးစိတ်ကို အာရုံစိုက်ရန်နှင့် လက်တွေ့ရလဒ်များကို အာရုံစိုက်ရန် လိုအပ်သည့် အခန်းကဏ္ဍများတွင် မကြာခဏ ထူးချွန်ကြသည်။ ၎င်းတို့သည် အပြောင်းအလဲ သို့မဟုတ် မရှင်းလင်းမှုများဖြင့် ရုန်းကန်ရနိုင်ပြီး ၎င်းတို့၏ တွေးခေါ်မှုတွင် အလွန်အမင်း ဝေဖန်ပိုင်းခြားခြင်း သို့မဟုတ် တင်းကျပ်ခြင်းအဖြစ် ကြုံတွေ့ရနိုင်သည်။")
        
        st.write(":violet[Strengths: ]")
        st.caption("Reliable, efficient, loyal, hard-working, and practical")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Inflexible, overly cautious, resistant to change, and risk-averse")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ISTJs may thrive in roles such as accounting, engineering, law enforcement, or project management, where their practical, detail-oriented approach is valued.")
        st.caption("ISTJ များသည် ၎င်းတို့၏လက်တွေ့ကျပြီး အသေးစိတ်ဆန်သောချဉ်းကပ်မှုကို တန်ဖိုးထားသည့်နေရာတွင် စာရင်းကိုင်၊ အင်ဂျင်နီယာ၊ ဥပဒေစိုးမိုးရေး သို့မဟုတ် ပရောဂျက်စီမံခန့်ခွဲမှုကဲ့သို့သော အခန်းကဏ္ဍများတွင် ရှင်သန်နိုင်သည်။")
        
        st.write(":violet[Famous persons:]")
        st.caption("George Washington, Queen Elizabeth II, Condoleezza Rice")
        
        st.write(":violet[]")
        st.caption("")
        st.caption("")
    #02    
    elif prediction == "ISFJ" :
        st.write("Your type is : :green[ISFJ - The Protector].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ISFJs are empathetic, caring, and responsible individuals who value tradition, order, and harmony. They tend to be dependable, supportive, and loyal, and are often motivated by a desire to help others.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ISFJs tend to be nurturing and supportive, often excelling in roles that require empathy and interpersonal skills. They may struggle with conflict or change and may be overly selfless, neglecting their own needs in favor of others.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Supportive, empathetic, hard-working, and practical")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Overly selfless, prone to avoiding conflict, and overly sensitive to criticism")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ISFJs may find fulfillment in roles such as teaching, counseling, nursing, or administrative work, where their caring and supportive nature is valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("")
        
        
       
    #03    
    elif prediction == "ISFJ" :
        st.write("Your type is : :green[ISFJ - The Protector].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ISFJs are empathetic, caring, and responsible individuals who value tradition, order, and harmony. They tend to be dependable, supportive, and loyal, and are often motivated by a desire to help others.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ISFJs tend to be nurturing and supportive, often excelling in roles that require empathy and interpersonal skills. They may struggle with conflict or change and may be overly selfless, neglecting their own needs in favor of others.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Empathetic, intuitive, idealistic, and creative")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Overly perfectionistic, overly sensitive to criticism, and prone to burnout")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ISFJs may find fulfillment in roles such as teaching, counseling, nursing, or administrative work, where their caring and supportive nature is valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Mahatma Gandhi, Nelson Mandela, Martin Luther King Jr")
        
        
       
    #04    
    elif prediction == "INTJ" :
        st.write("Your type is : :green[INTJ - The Mastermind].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("INTJs are strategic, analytical, and visionary individuals who value knowledge, innovation, and strategic thinking. They tend to be independent, logical, and decisive, with a strong sense of purpose and ambition.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("INTJs often excel in roles that require complex problem-solving and strategic thinking, such as entrepreneurship or management. They may struggle with interpersonal dynamics or may come across as overly analytical or critical in their thinking.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Analytical, strategic, independent, and confident")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Arrogant, overly critical, and prone to overthinking")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("INTJs may find fulfillment in roles such as law, engineering, business, or technology, where their strategic thinking and analytical skills are valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Elon Musk, Stephen Hawking, Mark Zuckerberg")
        
        
       
    #05    
    elif prediction == "ISTP" :
        st.write("Your type is : :green[ISTP - The Craftsman].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ISTPs are practical, logical, and analytical individuals who are adept at troubleshooting and problem-solving. They are hands-on and often have a talent for mechanics or engineering.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ISTPs tend to be adaptable and independent, with a focus on action rather than words. They may be risk-takers and impulsive at times, and can sometimes come across as aloof or unemotional.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Resourceful, adaptable, independent, and logical")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Impulsive, insensitive, prone to risk-taking, and emotionally reserved")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ISTPs may excel in careers such as engineering, mechanics, law enforcement, or construction, where their hands-on problem-solving skills are valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Clint Eastwood, Amelia Earhart, Bruce Lee")
        
        
       
    #06    
    elif prediction == "ISFP" :
        st.write("Your type is : :green[ISFP - The Composer].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ISFPs are sensitive, creative, and artistic individuals who value authenticity and individuality. They have a keen eye for aesthetics and may excel in artistic pursuits.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ISFPs tend to be reserved and compassionate, and may be motivated by a desire to make a difference in the world. They may struggle with decision-making and may become overly focused on details.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Artistic, empathetic, gentle, and compassionate")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Prone to mood swings, indecisive, overly sensitive to criticism, and conflict-averse")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ISFPs may thrive in careers such as art, music, writing, counseling, or social work, where their creative and empathetic qualities are valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Bob Dylan, Britney Spears, Prince")
        
        
       
    #07    
    elif prediction == "INFP" :
        st.write("Your type is : :green[INFP - The Healer].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("INFPs are idealistic, compassionate, and introspective individuals who value authenticity and personal growth. They are creative and may have a talent for writing or the arts.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("INFPs tend to be empathetic and intuitive, with a focus on personal values and meaning. They may struggle with assertiveness and may be prone to self-doubt.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Empathetic, idealistic, creative, and insightful")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Overly idealistic, prone to self-doubt, and indecisive")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("INFPs may excel in careers such as counseling, writing, teaching, social work, or creative arts, where their empathy and creativity are valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("J.R.R. Tolkien, William Shakespeare, Princess Diana")
        
        
       
    #08    
    elif prediction == "INTP" :
        st.write("Your type is : :green[INTP - The Architect].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("INTPs are analytical, logical, and theoretical individuals who are skilled at problem-solving and critical thinking. They are independent and value intellectual pursuits.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("INTPs tend to be curious and objective, with a focus on exploring new ideas and theories. They may struggle with emotional expression and may become overly critical or detached.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Analytical, logical, independent, and creative")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Prone to overthinking, insensitive, and overly critical")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("INTPs may thrive in careers such as computer programming, research, engineering, or scientific fields, where their analytical and theoretical approach is valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Albert Einstein, Abraham Lincoln, Thomas Jefferson")
        
        
       
    #09    
    elif prediction == "ESTP" :
        st.write("Your type is : :green[ESTP - The Dynamo].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ESTPs are energetic, outgoing, and action-oriented individuals who enjoy taking risks and living in the moment. They are adaptable and thrive on excitement and new experiences.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ESTPs tend to be competitive and confident, with a focus on practical results. They may struggle with long-term planning and may become impulsive or reckless at times.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Confident, practical, adventurous, and adaptable")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Impulsive, insensitive, and risk-prone")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ESTPs may excel in careers such as sales, entrepreneurship, athletics, or law enforcement, where their risk-taking and action-oriented qualities are valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Madonna, Jack Nicholson, Bruce Willis")
        
        
       
    #10    
    elif prediction == "ESFP" :
        st.write("Your type is : :green[ESFP - The Performer].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ESFPs are outgoing, friendly, and spontaneous individuals who enjoy being the center of attention. They are often talented in the performing arts or other creative pursuits.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ESFPs tend to be fun-loving and optimistic, with a focus on living in the moment and enjoying life. They may struggle with long-term planning and may become easily distracted.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Spontaneous, enthusiastic, friendly, and outgoing")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Impulsive, prone to drama, and easily distracted")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ESFPs may thrive in careers such as acting, music, event planning, or hospitality, where their creativity and social skills are valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Marilyn Monroe, Elvis Presley, Katy Perry")
        
        
       
    #11    
    elif prediction == "ENFP" :
        st.write("Your type is : :green[ENFP - The Champion].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ENFPs are enthusiastic, imaginative, and charismatic individuals who value creativity and innovation. They are often skilled at brainstorming and problem-solving.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ENFPs tend to be empathetic and adaptable, with a focus on personal growth and authenticity. They may struggle with follow-through and may become overly idealistic at times.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Enthusiastic, empathetic, creative, and optimistic")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Impulsive, prone to overthinking, and overly sensitive to criticism")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ENFPs may excel in careers such as writing, counseling, marketing, or entrepreneurship, where their creativity and innovative thinking are valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Walt Disney, Robin Williams, Ellen DeGeneres")
        
        
       
    #12    
    elif prediction == "ENTP" :
        st.write("Your type is : :green[ENTP - The Visionary].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ENTPs are curious, analytical, and inventive individuals who enjoy exploring new ideas and possibilities. They are often skilled at problem-solving and critical thinking.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ENTPs tend to be independent and adaptable, with a focus on exploring new ideas and challenging assumptions. They may struggle with follow-through and may become argumentative or critical at times.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Analytical, creative, confident, and independent")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Arrogant, insensitive, and prone to procrastination")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ENTPs may thrive in careers such as engineering, science, law, or entrepreneurship, where their analytical and inventive approach is valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Benjamin Franklin, Steve Jobs, Richard Branson")
        
        
       
    #13    
    elif prediction == "ESTJ" :
        st.write("Your type is : :green[ESTJ - The Supervisor].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ESTJs are practical, decisive, and organized individuals who value efficiency and productivity. They are often respected for their leadership skills and ability to make tough decisions.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ESTJs tend to be responsible and dependable, with a focus on results and practicality. They may struggle with change and may become overly critical or inflexible at times.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Practical, logical, efficient, and dependable")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Inflexible, overly controlling, and resistant to change")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ESTJs may excel in careers such as business management, accounting, law, or engineering, where their practical and decisive approach is valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Jack Welch, Lyndon B. Johnson, Judge Judy")
        
        
       
    #14    
    elif prediction == "ESFJ" :
        st.write("Your type is : :green[ESFJ - The Provider].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ESFJs are warm, empathetic, and nurturing individuals who enjoy helping others. They are often skilled at building relationships and creating a sense of community.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ESFJs tend to be loyal and dependable, with a focus on caring for others and maintaining harmony. They may struggle with conflict and may become overly concerned with others' opinions of them.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Warm, empathetic, responsible, and dependable")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Overly selfless, prone to avoiding conflict, and overly sensitive to criticism")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ESFJs may thrive in careers such as nursing, teaching, social work, or event planning, where their caring and nurturing qualities are valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Taylor Swift, Queen Elizabeth II, Barbara Walters")
        
        
       
    #15    
    elif prediction == "ENFJ" :
        st.write("Your type is : :green[ENFJ - The Teacher].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ENFJs are charismatic, empathetic, and persuasive individuals who enjoy helping others reach their potential. They are often skilled at leading and motivating groups of people.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ENFJs tend to be idealistic and compassionate, with a focus on understanding and connecting with others. They may struggle with setting boundaries and may become overly involved in others' lives.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Empathetic, charismatic, visionary, and inspiring")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Overly idealistic, prone to burnout, and overly sensitive to criticism")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ENFJs may excel in careers such as counseling, teaching, coaching, or nonprofit management, where their leadership and interpersonal skills are valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Martin Luther King Jr., Oprah Winfrey, Tony Robbins")
        
        
       
    #16    
    elif prediction == "ENTJ" :
        st.write("Your type is : :green[ENTJ - The Commander].")
        
        st.write(":violet[Characteristics: ]")
        st.caption("ENTJs are confident, strategic, and decisive individuals who enjoy taking charge and leading others. They are often skilled at setting and achieving goals.")
        st.caption("")
        
        st.write(":violet[Tendencies: ]")
        st.caption("ENTJs tend to be analytical and results-oriented, with a focus on efficiency and productivity. They may struggle with empathy and may come across as overly assertive or demanding at times.")
        st.caption("")
        
        st.write(":violet[Strengths: ]")
        st.caption("Strategic, confident, decisive, and assertive")
        st.caption("")
        
        st.write(":violet[Weaknesses:]")
        st.caption("Overly controlling, impatient, and insensitive")
        st.caption("")
        
        st.write(":violet[Career recommendations:]")
        st.caption("ENTJs may thrive in careers such as business management, law, politics, or entrepreneurship, where their leadership and strategic thinking are valued.")
        st.caption("")
        
        st.write(":violet[Famous persons:]")
        st.caption("Napoleon Bonaparte, Steve Jobs, Margaret Thatcher")
              
        
    else:
        st.write(":red[Abnormal Answer!]")



    