import {Box, Container, Tab, Tabs,} from '@mui/material';
import React, {useState} from 'react';
import UploadImageTab from './UploadImage/UploadImageTab';
import TabPanel from './TabPanel.js';

const UploadPage = () => {
    const [tab, setTab] = useState(0);
    return (
        <Container>
            <Box marginTop={5} sx={{width: '100%'}}>
                <Box sx={{borderBottom: 1, borderColor: 'divider'}}>
                    <Tabs value={tab} onChange={(e, newValue) => setTab(newValue)}>
                        <Tab label="Upload SVG image"/>
                        <Tab label="Insert XML code"/>
                    </Tabs>
                </Box>
                <TabPanel value={tab} index={0}>
                    <UploadImageTab/>
                </TabPanel>
                <TabPanel value={tab} index={1}>
                    {/*<InsertCodeTab />*/}
                </TabPanel>
            </Box>
        </Container>

    );
}

export default UploadPage