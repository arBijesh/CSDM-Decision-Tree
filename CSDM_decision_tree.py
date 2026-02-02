import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="CSDM Classifier Pro", page_icon="🧊", layout="wide")

# --- STYLES ---
st.markdown("""
<style>
    .design { border-left: 6px solid #00B5AD; background-color: #F0FBFC; padding: 15px; }
    .manage { border-left: 6px solid #F2711C; background-color: #FEF6F1; padding: 15px; }
    .consume { border-left: 6px solid #21BA45; background-color: #F0FDF4; padding: 15px; }
    .explanation-box { background-color: #fff; border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    .example-list { background-color: #fafafa; padding: 10px; border-radius: 5px; border: 1px dashed #ccc; }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
if 'step' not in st.session_state: st.session_state.step = 'start'

def navigate(next_step):
    st.session_state.step = next_step
    st.rerun()

def restart():
    st.session_state.step = 'start'
    st.rerun()

# --- HEADER ---
col1, col2 = st.columns([1, 6])
with col1: st.title("🧊")
with col2: 
    st.title("CSDM Classifier Tool")
    st.caption("Standardized Classification & Naming Assistant")
st.divider()

step = st.session_state.step

# ---------------------------------------------------------
# STEP 1: BUSINESS CAPABILITY (Now with Layman Explanation)
# ---------------------------------------------------------
if step == 'start':
    st.subheader("Step 1: Business Capability Check")
    st.markdown("### Is this a high-level business 'Ability' or 'Function'?")
    
    st.markdown("""
    <div class="explanation-box">
        <h4>🛑 Layman's Terms: The "Resume Skill" Analogy</h4>
        <p>Think of a Business Capability as a <strong>Skill on a Resume</strong>.</p>
        <ul>
            <li><strong>The Skill:</strong> "Project Management" (This is the Capability).</li>
            <li><strong>The Tool:</strong> "Microsoft Excel" or "Jira" (This is the Application).</li>
        </ul>
        <hr>
        <h4>🧪 The "Stable Strategy" Test</h4>
        <p>If we fired the entire IT department and threw away all computers, would the business <em>still need to do this</em>?</p>
        <ul>
            <li><strong>YES:</strong> "We still need to do <em>Recruiting</em>." (This is a <strong>Business Capability</strong>).</li>
            <li><strong>NO:</strong> "We cannot do <em>Zoom</em> without computers." (Zoom is just a tool/Application).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    if c1.button("YES (It's a Strategic Ability)"): navigate('res_bus_cap')
    if c2.button("NO (It's something else)"): navigate('check_portfolio')

# ---------------------------------------------------------
# STEP 2: SERVICE PORTFOLIO
# ---------------------------------------------------------
elif step == 'check_portfolio':
    st.subheader("Step 2: Service Portfolio Check")
    st.markdown("### Is this the 'Menu' or the 'Food'?")
    
    st.markdown("""
    <div class="explanation-box">
        <h4>🛑 Layman's Terms: The Restaurant Analogy</h4>
        <p>A <strong>Service Portfolio</strong> is the <strong>Menu</strong> (e.g., "The Lunch Menu").</p>
        <ul>
            <li>You cannot "eat" the Menu. You cannot "fix" the Menu.</li>
            <li>It is just a container that lists the available services.</li>
        </ul>
        <p><em>If your item is just a grouping folder for reporting, say YES.</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    if c1.button("YES (It is the Menu/Portfolio)"): navigate('res_svc_port')
    if c2.button("NO (It is the Food/Service)"): navigate('check_software')

# ---------------------------------------------------------
# STEP 3: BUSINESS APPLICATION
# ---------------------------------------------------------
elif step == 'check_software':
    st.subheader("Step 3: Business Application Check")
    st.markdown("### Is this a named Software Product we buy and track?")
    st.info("The 'Brand Name' in our inventory.")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Business App)"): navigate('res_bus_
