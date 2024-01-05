import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import seaborn as sns

st.sidebar.title("Your secret lover finder")

uploaded_file= st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data= bytes_data.decode("utf-8")
    df= preprocessor.preprocess(data)


    user_list= df['user'].unique().tolist()
    user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user= st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show your love stats"):

        num_messages, words, num_media_messages,links= helper.fetch_stats(selected_user,df)

        col1, col2, col3, col4 = st.columns(4)

        st.title('Top Statsticks')

        with col1:
            st.header("total messages")
            st.title(num_messages)

        with col2:
            st.header("total words")
            st.title(words)

        with col3:
            st.header(" NO. of media shared")
            st.title(num_media_messages)

        with col4:
            st.header("links shared")
            st.title(links)

        st.title("activity monthly")
        timeline_monthly,timeline_daily= helper.activity(selected_user,df)
        if timeline_monthly is not None:
            if 'time_month' in timeline_monthly.columns and 'message' in timeline_monthly.columns:
                fig, ax = plt.subplots()
                ax.plot(timeline_monthly['time_month'], timeline_monthly['message'])
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            else:
                print("Columns 'time' and 'message' not found in the timeline DataFrame.")
        else:
            print("Timeline DataFrame is None. Check your data loading process.")

        st.title("activity daily")
        fig, ax = plt.subplots()
        ax.plot(timeline_daily['only_date'], timeline_daily['message'],color='purple')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title('activity map')
        col1,col2= st.columns(2)

        with col1:
            st.header("bussy weekdays")
            busy_day=helper.weekly_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='yellow')
            st.pyplot(fig)

        with col2:
            st.header("bussy months")
            busy_day = helper.monthly_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values,color='red')
            st.pyplot(fig)

        st.title("bussy timings")
        activity_heatmap=helper.activity_heatmap(selected_user,df)
        fig,ax=plt.subplots()
        ax=sns.heatmap(activity_heatmap)
        st.pyplot(fig)

        if selected_user== 'Overall':
            st.title("most bussy user")
            x,new_df= helper.most_busy_users(df)
            fig, ax= plt.subplots()

            col1, col2= st.columns(2)

            with col1:
                ax.bar(x.index, x.values)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

        st.title("your fav stuff")
        df_wc= helper.create_wordcloud(selected_user,df)
        fig,ax= plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)


        st.title("your fav words")
        most_common_df= helper.most_common_words(selected_user,df)
        fig,ax= plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1],color='orange')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # emoji_df=helper.number_emoji(selected_user,df)
        # st.title("Emojiiiiiiii")
        #
        # col1,col2= st.columns(2)
        #
        # with col1:
        #     st.dataframe(emoji_df)
        #
        # with col2:
        #     fig,ax= plt.subplots()






