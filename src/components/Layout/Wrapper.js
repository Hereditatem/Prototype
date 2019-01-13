import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import { withStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import ArrowBack from '@material-ui/icons/ArrowBack'
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import Badge from '@material-ui/core/Badge';
import NotificationsIcon from '@material-ui/icons/Notifications';
import styles from './WrapperStyle'

const AppBarWrapper = ({classes, title = 'Hereditatem', children}) => (
    <AppBar
        position="absolute"
        className={classNames(classes.appBar)}
    >
        <Toolbar className={classes.toolbar}>
            <IconButton
                color="inherit"
                aria-label="Open drawer"              
                className={classNames(
                classes.menuButton
                )}
                >
                <ArrowBack />
                </IconButton>
            <Typography
                component="h1"
                variant="h6"
                color="inherit"
                noWrap
                className={classes.title}
            >
                {title}
            </Typography>
            {children}
            <IconButton color="inherit">
                <Badge badgeContent={4} color="secondary">
                    <NotificationsIcon />
                </Badge>
            </IconButton>
        </Toolbar>
    </AppBar>
);

const MainWraper = ({classes, children}) => (
    <main className={classes.content}>
        {children}
    </main>
);

class Wrapper extends React.Component {
    render() {
        const { classes, children } = this.props;

        return (
            <div className={classes.root}>
                {children}
            </div>
        );
    }
}
Wrapper.propTypes = {
    classes: PropTypes.object.isRequired,
    children: PropTypes.array,
};

Wrapper.Main = withStyles(styles)(MainWraper); 
Wrapper.AppBar = withStyles(styles)(AppBarWrapper);


export default withStyles(styles)(Wrapper);