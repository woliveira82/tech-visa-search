window.onload = _ => {
    let btn_companies = document.getElementById("show-company");
    let btn_jobs = document.getElementById("show-job");
    let tb_company = document.getElementById("tb-company");
    let tb_job = document.getElementById("tb-job");

    btn_companies.onclick = function () {
        this.className = 'clicked';
        btn_jobs.className = 'unclicked';
        tb_company.style.display = "block";
        tb_job.style.display = "none";
    };
    
    btn_jobs.onclick = function () {
        this.className = 'clicked';
        btn_companies.className = 'unclicked';
        tb_company.style.display = "none";
        tb_job.style.display = "block";
    };

    let i_companies = document.getElementById("load-company");
    let i_jobs = document.getElementById("load-job");
    
    i_companies.onchange = function(e) {
        console.log(e);
        console.log(this);
    }
    
    i_jobs.onchange = function(e) {
        console.log(e);
        console.log(this);
    }
};
