import { Button, Card, CardContent, Grid } from '@material-ui/core';
import { Form, Formik } from 'formik';
import React from 'react';
import { array, object, string } from 'yup';
import  DragNDrop from './DragNDrop';

const UplaodImageTab = () => {
  const initialData = { files: [] }
  
  const validationSchema = object({
    files: array(
      object({
        url: string().required(),
      })
    ).min(1, 'Minimum of 1 SVG file'),
  })

  const submitForm = (values) => {
    console.log('values', values);
    return new Promise((res) => setTimeout(res, 2000));
  }

  return (
    <Card>
      <CardContent>
        <Formik
          initialValues={initialData}
          validationSchema={validationSchema}
          onSubmit={submitForm}
        >
          {({ values, errors, isValid, isSubmitting }) => (
            <Form>
              <Grid container spacing={2} direction="column">
                <DragNDrop name="files" />
                <Grid item>
                  <Button
                    variant="contained"
                    color="primary"
                    disabled={!isValid || isSubmitting}
                    type="submit"
                  >
                    Submit
                  </Button>
                </Grid>
              </Grid>
              <pre>{values && JSON.stringify({ values, errors }, null, 4)}</pre>
            </Form>
          )}
        </Formik>
      </CardContent>
    </Card>
  );
}

export default UplaodImageTab