import { TextareaAutosize } from '@mui/material';
import React, {useState, useEffect} from 'react';
import { useField } from 'formik';

const CodeInput = ({name}) => {
    const [_, __, helpers] = useField(name);
    const [code, setCode] = useState('');

    useEffect(() => {
        helpers.setValue(code);
        // helpers.setTouched(true);
      }, [code]);

    return(
        <TextareaAutosize
            placeholder="<svg>...</svg>"
            style={{ width: '100%', height: '20vh' }}
            value={code}
            onChange={(event) => setCode(event.target.value)}
        />
    )
}

export default CodeInput