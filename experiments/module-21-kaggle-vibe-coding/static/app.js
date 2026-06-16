document.addEventListener('DOMContentLoaded', () => {
    console.log('[Workbench] App loaded in safe mode.');

    const btnPlan = document.getElementById('btnPlan');
    const btnRun = document.getElementById('btnRun');
    const promptInput = document.getElementById('promptInput');
    
    const planPanel = document.getElementById('planPanel');
    const planOutput = document.getElementById('planOutput');
    
    const agentPanel = document.getElementById('agentPanel');
    const agentOutput = document.getElementById('agentOutput');

    btnPlan.addEventListener('click', async () => {
        const prompt = promptInput.value.trim();
        if (!prompt) {
            alert('Please enter a prompt.');
            return;
        }

        console.log('[Workbench] Plan requested for prompt:', prompt);
        btnPlan.disabled = true;
        btnPlan.textContent = 'Planning...';

        try {
            const response = await fetch('/api/plan', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt })
            });

            const data = await response.json();
            
            planPanel.classList.remove('hidden');
            if (response.ok) {
                planOutput.textContent = JSON.stringify(data, null, 2);
                btnRun.disabled = false;
                console.log('[Workbench] Local-only execution confirmed for plan.');
            } else {
                planOutput.textContent = `Error: ${data.error}`;
                btnRun.disabled = true;
            }
        } catch (error) {
            console.error('[Workbench] Network error:', error);
            planOutput.textContent = 'Network error occurred.';
        } finally {
            btnPlan.disabled = false;
            btnPlan.textContent = 'Generate Plan';
        }
    });

    btnRun.addEventListener('click', async () => {
        const prompt = promptInput.value.trim();
        
        console.log('[Workbench] Agent run requested.');
        btnRun.disabled = true;
        btnRun.textContent = 'Running...';
        agentPanel.classList.add('hidden');

        try {
            const response = await fetch('/api/agent', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt })
            });

            const data = await response.json();
            
            agentPanel.classList.remove('hidden');
            if (response.ok) {
                agentOutput.textContent = JSON.stringify(data, null, 2);
                console.log('[Workbench] Local-only execution confirmed for agent.');
            } else {
                agentOutput.textContent = `Error: ${data.error}`;
            }
        } catch (error) {
            console.error('[Workbench] Network error:', error);
            agentOutput.textContent = 'Network error occurred.';
        } finally {
            btnRun.disabled = false;
            btnRun.textContent = 'Run Agent';
        }
    });
});
