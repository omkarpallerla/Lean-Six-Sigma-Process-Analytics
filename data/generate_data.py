import pandas as pd
import numpy as np
np.random.seed(42)

n = 500
brands = ['AlphaBrand', 'BetaBrand', 'GammaBrand']
regions = ['North', 'South', 'East', 'West']
stages = ['Draft', 'Review', 'Legal', 'Approval', 'Sent']

data = []
for i in range(n):
    brand = np.random.choice(brands)
    region = np.random.choice(regions)
    # Before improvement: mean ~31.6 days
    if i < 350:
        cycle_time = np.random.normal(31.6, 6.2)
    else:
        # After improvement: mean ~26.9 days
        cycle_time = np.random.normal(26.9, 4.8)
    cycle_time = max(5, round(cycle_time, 1))
    sla_breach = 1 if cycle_time > 35 else 0
    rework = 1 if np.random.random() < (0.12 if i < 350 else 0.02) else 0
    data.append({
        'proposal_id': f'PROP-{1000+i}',
        'brand': brand,
        'region': region,
        'cycle_time_days': cycle_time,
        'sla_breach': sla_breach,
        'rework_flag': rework,
        'phase': 'Before' if i < 350 else 'After',
        'submission_date': pd.Timestamp('2024-01-01') + pd.Timedelta(days=i//2)
    })

df = pd.DataFrame(data)
df.to_csv('proposals.csv', index=False)
print(f"Generated {len(df)} records")
print(df.groupby('phase')['cycle_time_days'].agg(['mean','std','count']))
