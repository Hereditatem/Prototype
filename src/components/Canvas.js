import React from 'react';
import Draggable from 'react-draggable';
import A3 from '../assets/images/A3.png'

const MOVE_TOOL_ID = "drag";
const ROTATE_TOOL_ID = "rotate";

class MoveTool extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            activeDrags: null
        };
    }

    render() {
        const styles = {
            position: 'relative',
            width: 100,
            heigh: 100
        };
        return (
            <Draggable
                handle=".handle"
                defaultPosition={{ x: 0, y: 0 }}
                position={null}>
                <div className="handle" style={styles}>
                    {this.props.children}
                </div>
            </Draggable>
        );
    }
}

class RotateTool extends React.Component {
    render() {
        const styles = {
            position: "absolute",
            top: -50,
            left: -50,
            width: 200,
            height: 200,
            border: '1px gray dashed',
            borderRadius: 100
        };
        return (
            <div className="rotate-tool" >
                <div style={styles} />
                {this.props.children}
            </div>
        );
    }
}

class Fragment extends React.Component {

    onFragmentMove(moveEventData) {
        this.props.fragment.y += moveEventData.deltaY;
        this.props.fragment.x += moveEventData.deltaX;
    }

    onFragmentRotated(rotateEvent) {

    }

    render() {
        const styles = {
            position: 'abosulte',
            width: 100,
            heigh: 100,
            filter: this.props.isSelected ? "drop-shadow(0px 0px 0.25rem crimson)" : null,
        }
        const ImageStyles = {
            width: 100,
            heigh: 100,
            userDrag: 'none',
            userSelect: 'none',
            mozUserSelect: 'none',
            webkitUserDrag: 'none',
            webkitUserSelect: 'none',
            msUserSelect: 'none',
        }
        return (
            <MoveTool OnMoved={(data) => this.onFragmentMove(data)}>
                <RotateTool>
                    <img style={ImageStyles} src={A3} alt="A3" />
                </RotateTool>
            </MoveTool >
        );
    }
}

class Canvas extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedFragment: null
        };
    }
    setSelectedFragment(fragment) {
        this.setState({ selectedFragment: fragment })
    }

    render() {
        const styles = {
            position: "relative",
        }
        return (
            <div className="canvas" style={styles}>
                {this.props.fragments.map(fragment => (
                    <Fragment
                        fragment={fragment}
                        isSelected={fragment === this.state.selectedFragment}
                    />))}
            </div>);
    }
};
// onClick={() => this.setSelectedFragment(fragment)}
export { MOVE_TOOL_ID as DRAG_TOOL_ID, ROTATE_TOOL_ID }
export default Canvas;