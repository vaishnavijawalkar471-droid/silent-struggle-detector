import streamlit as st
import pandas as pd

# ============================================================================
# SECTION 1: Detection Logic (Rule-Based)
# ============================================================================

def detect_silent_struggle(rating, comment):
    """
    Analyzes a single feedback entry and returns a label.
    
    Args:
        rating (int): User rating from 1-5
        comment (str): User's text comment
    
    Returns:
        str: One of "Silent Struggle", "Strong Negative", or "Clear Opinion"
    """
    # List of vague/hesitant words that indicate uncertainty
    vague_words = [
        'okay', 'fine', 'maybe', 'guess', 'not sure', 
        'works', 'alright', 'sort of', 'kind of', 'i think',
        'decent', 'acceptable', 'passable', 'tolerable'
    ]
    
    # Convert comment to lowercase for easier matching
    comment_lower = comment.lower()
    
    # Check if any vague words appear in the comment
    has_vague_language = any(word in comment_lower for word in vague_words)
    
    # Apply detection rules
    if rating >= 4 and has_vague_language:
        return "🟡 Silent Struggle"
    elif rating <= 2:
        return "🔴 Strong Negative"
    else:
        return "🟢 Clear Opinion"


# ============================================================================
# SECTION 2: Streamlit App UI
# ============================================================================

def main():
    # App title and description
    st.title("Silent Struggle Detector 🔍")
    st.markdown("""
    ### What is SILENT STRUGGLE?
Welcome in. Sometimes positive ratings don’t capture the full experience. When feedback sounds polite or uncertain despite high scores, it can point to concerns users hesitate to voice. We help you notice what’s left unsaid—so every experience can truly improve.
    
     Examples:
     ⭐⭐⭐⭐⭐  "It's okay, I guess it works fine" → Silent Struggle!
     ⭐⭐⭐⭐    "Maybe it's alright, not sure yet" → Silent Struggle!
     ⭐⭐       "Terrible experience".             → Strong Negative (honest feedback)
     ⭐⭐⭐⭐⭐  "Amazing product!"                 → Clear Opinion (genuine praise)
    """)
    
    st.markdown("---")
    
    # File uploader
    st.subheader("📂 Step 1: Upload Your Feedback Data")
    st.info("Upload a CSV file with columns: id, rating, comment, date")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    # If a file is uploaded, process it
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Validate that required columns exist
        required_columns = ['id', 'rating', 'comment', 'date']
        if not all(col in df.columns for col in required_columns):
            st.error(f"❌ Missing required columns! Your CSV must have: {', '.join(required_columns)}")
            return
        
        st.success(f"✅ File loaded successfully! Found {len(df)} feedback entries.")
        
        # Apply detection to each row
        df['Detection'] = df.apply(
            lambda row: detect_silent_struggle(row['rating'], row['comment']), 
            axis=1
        )
        
        # ====================================================================
        # SECTION 3: Display Results
        # ====================================================================
        
        st.markdown("---")
        st.subheader("📊 Step 2: View All Feedback")
        
        # Show the full table with detection results
        st.dataframe(
            df[['id', 'rating', 'comment', 'date', 'Detection']], 
            use_container_width=True
        )
        
        # Summary statistics
        col1, col2, col3 = st.columns(3)
        
        silent_count = len(df[df['Detection'] == '🟡 Silent Struggle'])
        negative_count = len(df[df['Detection'] == '🔴 Strong Negative'])
        clear_count = len(df[df['Detection'] == '🟢 Clear Opinion'])
        
        col1.metric("🟡 Silent Struggles", silent_count)
        col2.metric("🔴 Strong Negatives", negative_count)
        col3.metric("🟢 Clear Opinions", clear_count)
        
        # ====================================================================
        # SECTION 4: Highlight Silent Struggles
        # ====================================================================
        
        st.markdown("---")
        st.subheader("⚠️ Step 3: Silent Struggle Cases (Need Attention!)")
        
        # Filter only Silent Struggle entries
        silent_struggles = df[df['Detection'] == '🟡 Silent Struggle']
        
        if len(silent_struggles) > 0:
            st.warning(f"Found {len(silent_struggles)} cases where users gave high ratings but used hesitant language!")
            
            # Display each Silent Struggle case in a nice format
            for idx, row in silent_struggles.iterrows():
                with st.container():
                    st.markdown(f"""
                    **Feedback ID:** {row['id']}  
                    **Rating:** {'⭐' * int(row['rating'])} ({row['rating']}/5)  
                    **Date:** {row['date']}  
                    **Comment:** "{row['comment']}"
                    """)
                    st.markdown("---")
        else:
            st.success("🎉 No Silent Struggles detected! All feedback is clear.")
        
        # ====================================================================
        # SECTION 5: Download Results
        # ====================================================================
        
        st.markdown("---")
        st.subheader("💾 Step 4: Download Results")
        
        # Convert dataframe to CSV for download
        csv = df.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="📥 Download Analysis Results (CSV)",
            data=csv,
            file_name="silent_struggle_analysis.csv",
            mime="text/csv"
        )
        
    else:
        # Show example CSV format if no file uploaded
        st.info("👆 Upload a CSV file to get started!")
        
        st.markdown("### Example CSV Format:")
        example_df = pd.DataFrame({
            'id': [1, 2, 3],
            'rating': [5, 2, 4],
            'comment': [
                'It works fine, I guess',
                'Terrible product, waste of money',
                'Amazing experience, highly recommend!'
            ],
            'date': ['2024-01-15', '2024-01-16', '2024-01-17']
        })
        st.dataframe(example_df)


# ============================================================================
# SECTION 6: Run the App
# ============================================================================

if __name__ == "__main__":
    # Configure the page
    st.set_page_config(
        page_title="Silent Struggle Detector",
        page_icon="🔍",
        layout="wide"
    )
    
    # Run the main app
    main()