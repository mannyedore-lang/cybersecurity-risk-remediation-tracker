import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title='Cybersecurity Risk & Remediation Tracker', layout='wide')
DATA = Path(__file__).parent / 'data' / 'security_findings.csv'
df = pd.read_csv(DATA)

st.title('Cybersecurity Risk & Remediation Tracker')
st.caption('Executive view of security findings, severity, ownership, remediation status, and evidence readiness')

critical_high = int(df['severity'].isin(['Critical','High']).sum())
evidence_ready = int((df['evidence_ready'].str.lower() == 'yes').sum())
open_items = int((df['status'].str.lower() != 'closed').sum())

c1, c2, c3, c4 = st.columns(4)
c1.metric('Open Findings', open_items)
c2.metric('Critical / High', critical_high)
c3.metric('Evidence Ready', f'{evidence_ready}/{len(df)}')
c4.metric('Domains Affected', df['domain'].nunique())

st.subheader('Severity & Remediation Status')
col1, col2 = st.columns(2)
with col1:
    st.bar_chart(df['severity'].value_counts())
with col2:
    st.bar_chart(df['status'].value_counts())

st.subheader('Executive Remediation View')
show = df[['finding_id','domain','severity','owner','status','due_date','evidence_ready']].copy()
show.columns = ['Finding','Domain','Severity','Owner','Status','Due Date','Evidence Ready']
st.dataframe(show, use_container_width=True, hide_index=True)

st.subheader('Governance Questions')
st.markdown('''
- Which critical or high findings remain open?
- Which remediation items are approaching or past due?
- Which teams are carrying the largest remediation load?
- Where is evidence incomplete for audit or control validation?
- Which items require leadership escalation or formal risk acceptance?
''')

st.info('Security data is synthetic and provided solely for demonstration purposes.')
