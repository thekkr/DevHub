from django.shortcuts import render
from .queires import temp

# Create your views here.
def pf_jobs_detail(request):
    pf_df = temp()
    
    context = {
        'total_jobs': len(pf_df),
        'running_jobs_count': len(pf_df[pf_df['status'] == 'RUNNING']),
        'queued_jobs_count': len(pf_df[pf_df['status'] == 'QUEUED']),
        'pf_jobs': pf_df.to_dict('records')
    }
    return render(request, 'db_connectors/pf_job_details.html', context)