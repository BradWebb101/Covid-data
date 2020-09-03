import React from 'react';
import Grid from '@material-ui/core/Grid';

import HorizontalBarChart from './Charts/HorizontalBar';
import CaseSevenDays from './Charts/CaseSevenDays';

function Dashboard() {


    return (
            
        <Grid container spacing={3}>
        <Grid item xs={12}>
            <HorizontalBarChart />
        </Grid>

        <Grid item xs={12} sm={6}>
            <CaseSevenDays item xs={12} item xs={12}/>
        </Grid>

        <Grid item xs={12} sm={6}>
            <CaseSevenDays item xs={12} item xs={12}/>
        </Grid>

        <Grid item xs={1} sm={4}>
            <CaseSevenDays item xs={12} item xs={12}/>
        </Grid>
        <Grid item xs={1} sm={4}>
            <CaseSevenDays item xs={12} item xs={12}/>
        </Grid>
        <Grid item xs={1} sm={4}>
            <CaseSevenDays item xs={12} item xs={12}/>
        </Grid>

        </Grid>
      
    )
}

export default Dashboard
