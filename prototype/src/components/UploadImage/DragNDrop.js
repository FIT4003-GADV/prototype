import { Grid, makeStyles } from '@material-ui/core';
import { useField } from 'formik';
import React, { useCallback, useEffect, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import UploadWithProgress from './UploadWithProgress';
import UploadError from './UploadError'


let currentId = 0;
const getNewId = () => {
  return ++currentId;
}

const useStyles = makeStyles((theme) => ({
    dropzone: {
      border: `2px dashed ${theme.palette.primary.main}`,
      borderRadius: theme.shape.borderRadius,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: theme.palette.background.default,
      height: theme.spacing(10),
      outline: 'none',
    },
  }));

const DragNDrop = ({ name='files' }) => {
    const [_, __, helpers] = useField(name);
    const classes = useStyles();
    const [isHovering, setIsHovering] = useState(false);
    const [files, setFiles] = useState([]);

    const onDrop = useCallback((accFiles, rejFiles) => {
      accFiles.forEach((file) => 
      {
        let fileInfo = {imageInfo: file, errors: [], id: getNewId()}
        const reader1 = new FileReader()
        reader1.onload = (e) => {
          fileInfo = { ...fileInfo, xmlCode: e.target.result}
        };
        reader1.readAsText(file);

        const reader2 = new FileReader()
        reader2.onload = (e) => {
          setFiles((curr) => [...curr,{ ...fileInfo, dataUrl: e.target.result}])
        };
        reader2.readAsDataURL(file);
      });

      rejFiles.forEach((file) => (setFiles((curr) => [...curr, { ...file, imageInfo: file, id: getNewId() }])));

    }, []);
  
    useEffect(() => {
      helpers.setValue(files);
    }, [files]);
  
    const onUpload = (file, url) => {
      setFiles((curr) =>
        curr.map((fw) => {
          if (fw.file === file) {
            return { ...fw, url };
          }
          return fw;
        })
      );
    }
  
    const onDelete = (fileId) => {
      setFiles((files) => files.filter((file) => file.id !== fileId));
    }
  
    const { getRootProps, getInputProps } = useDropzone({
      onDrop,
      accept: ['.svg'],
      maxSize: 300 * 1024, // 300KB
    });
  
    return (
      <>
        <Grid item >
          <div
            onMouseOver={() => setIsHovering(true)}  
            onMouseLeave={() => setIsHovering(false)} 
            style={{backgroundColor: isHovering && '#E8E8E8', cursor: isHovering && 'pointer'}}
            {...getRootProps({ className: classes.dropzone })}
          >
            <input {...getInputProps()} />
            <p>Drag 'n' drop SVG image here, or click to select image</p>
          </div>
        </Grid>
  
        {files.map((fileWrapper) => (
          <Grid item key={fileWrapper.id}>
            {
              fileWrapper.errors.length ? 
              <UploadError
                file={fileWrapper}
                errors={fileWrapper.errors}
                onDelete={onDelete}
              /> : 
              <UploadWithProgress
                onDelete={onDelete}
                onUpload={onUpload}
                file={fileWrapper}
              />
            }
          </Grid>
        ))}
      </>
    );
  }

  export default DragNDrop
  